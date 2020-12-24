import os
import time
import os.path
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import shutil
import tinify
from settings import *
import threading

class MainWindow:

    THIS_FOLDER_G = ""
    if getattr(sys, "frozen", False):
        THIS_FOLDER_G = os.path.dirname(sys.executable)
    else:
        THIS_FOLDER_G = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, root):
        self.root = root

        # Thread for Compressing the Images.
        self.compress = None
        # Thread for Stoping the Compressing thread process.
        self.stop = None
        self.stopFlag = False

        self._folder_url1 = tk.StringVar()
        self._folder_url2 = tk.StringVar()
        self._api_key = tk.StringVar()
        self._status = tk.StringVar()
        self.raw_images_dir = ""
        self.save_dir = ""
        self.abs_image_path = ""
        self.raw_images = []
        self._status.set("---")
        self.SUPPORTED_FORMATS = ('jpg', 'jpeg', 'png')

        root.title("Compresssio")
        root.configure(bg="#eeeeee")

        try:
            icon_img = tk.Image(
                "photo",
                file=self.THIS_FOLDER_G + "./files/compresssio.ico"
            )
            root.call(
                "wm",
                "iconphoto",
                root._w,
                icon_img
            )
        except Exception:
            pass

        self.menu_bar = tk.Menu(
            root,
            bg="#eeeeee",
            relief=tk.FLAT
        )
        self.menu_bar.add_command(
            label="Help!",
            command=self.show_help_callback
        )
        self.menu_bar.add_command(
            label="About",
            command=self.show_about
        )

        root.configure(
            menu=self.menu_bar
        )

        self.file_entry_label1 = tk.Label(
            root,
            text="Enter Input Folder Path:",
            bg="#eeeeee",
            anchor=tk.W
        )
        self.file_entry_label1.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=0,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.file_entry1 = tk.Entry(
            root,
            textvariable=self._folder_url1,
            bg="#fff",
            exportselection=0,
            relief=tk.FLAT
        )
        self.file_entry1.grid(
            padx=15,
            pady=6,
            ipadx=8,
            ipady=8,
            row=1,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.select_btn1 = tk.Button(
            root,
            text="SELECT INPUT FOLDER",
            command=self.selectfolder1_callback,
            width=42,
            bg="#3498db",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.select_btn1.grid(
            padx=15,
            pady=8,
            ipadx=24,
            ipady=6,
            row=2,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.file_entry_label2 = tk.Label(
            root,
            text="Enter Output Folder Path:",
            bg="#eeeeee",
            anchor=tk.W
        )
        self.file_entry_label2.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=3,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.file_entry2 = tk.Entry(
            root,
            textvariable=self._folder_url2,
            bg="#fff",
            exportselection=0,
            relief=tk.FLAT
        )
        self.file_entry2.grid(
            padx=15,
            pady=6,
            ipadx=8,
            ipady=8,
            row=4,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.select_btn2 = tk.Button(
            root,
            text="SELECT OUTPUT FOLDER",
            command=self.selectfolder2_callback,
            width=42,
            bg="#3498db",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.select_btn2.grid(
            padx=15,
            pady=8,
            ipadx=24,
            ipady=6,
            row=5,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.key_entry_label = tk.Label(
            root,
            text="Enter Your API Key:",
            bg="#eeeeee",
            anchor=tk.W
        )
        self.key_entry_label.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=6,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.key_entry = tk.Entry(
            root,
            textvariable=self._api_key,
            bg="#fff",
            exportselection=0,
            relief=tk.FLAT
        )
        self.key_entry.grid(
            padx=15,
            pady=6,
            ipadx=8,
            ipady=8,
            row=7,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.compress_btn = tk.Button(
            root,
            text=" START COMPRESS",
            command=self.compress_callback,
            bg="#27ae60",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.compress_btn.grid(
            padx=15,
            pady=8,
            ipadx=24,
            ipady=6,
            row=8,
            column=0,
            columnspan=2,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.stop_btn = tk.Button(
            root,
            text="STOP",
            command=self.stop_callback,
            bg="#aaaaaa",
            fg="#ffffff",
            bd=2,
            state='disabled',
            relief=tk.FLAT
        )
        self.stop_btn.grid(
            padx=15,
            pady=8,
            ipadx=24,
            ipady=6,
            row=8,
            column=2,
            columnspan=2,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.reset_btn = tk.Button(
            root,
            text="CLEAR STATUS",
            command=self.reset_callback,
            bg="#717d7e",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.reset_btn.grid(
            padx=15,
            pady=(4, 12),
            ipadx=24,
            ipady=6,
            row=9,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.status_label = tk.Label(
            root,
            textvariable=self._status,
            bg="#eeeeee",
            anchor=tk.W,
            justify=tk.LEFT,
            relief=tk.FLAT,
            wraplength=350
        )
        self.status_label.grid(
            padx=12,
            pady=(0, 12),
            ipadx=0,
            ipady=1,
            row=10,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

    def selectfolder1_callback(self):
        try:
            name = filedialog.askdirectory()
            self._folder_url1.set(name)
        except Exception as e:
            self._status.set(e)
            self.status_label.update()

    def selectfolder2_callback(self):
        try:
            name = filedialog.askdirectory()
            self._folder_url2.set(name)
        except Exception as e:
            self._status.set(e)
            self.status_label.update()
    
    def enable(self):

        self.stop_btn['bg'] = "#aaaaaa"
        self.stop_btn['state'] = 'disabled'
        self.compress_btn['state'] = 'normal'
        self.compress_btn['bg'] = '#27ae60'
        self.reset_btn['bg'] = "#717d7e"
        self.reset_btn['state'] = 'normal'
        self.file_entry1['state'] = 'normal'
        self.file_entry2['state'] = 'normal'
        self.select_btn1['state'] = 'normal'
        self.select_btn2['state'] = 'normal'
        self.select_btn1['bg'] = '#3498db'
        self.select_btn2['bg'] = '#3498db'

    def disable(self):

        self.compress_btn['bg'] = "#aaaaaa"
        self.compress_btn['state'] = 'disabled'
        self.reset_btn['bg'] = "#aaaaaa"
        self.reset_btn['state'] = 'disabled'
        self.stop_btn['bg'] = "#e74c3c"
        self.stop_btn['state'] = 'normal'
        self.file_entry1['state'] = 'disabled'
        self.file_entry2['state'] = 'disabled'
        self.select_btn1['state'] = 'disabled'
        self.select_btn2['state'] = 'disabled'
        self.select_btn1['bg'] = '#aaaaaa'
        self.select_btn2['bg'] = '#aaaaaa'

    def show_help_callback(self):
        messagebox.showinfo(
            "Help!",
            """1. Click SELECT INPUT FOLDER Button to select the INPUT FOLDER which contains all the Images to be Compressed/Optimized.
2. Click SELECT OUTPUT FOLDER Button to select the OUTPUT FOLDER which will contain all the the Compressed/Optimized Images. (After Compression)
3. Enter Your API Key from TINYPNG Website. If you don't have one in possession then you can find on this website https://tinypng.com/developers/
4. Hit the COMPRESS Button and the INPUT FOLDER containing Supported Image Formats will be Compressed and saved in the OUTPUT FOLDER.
5. Click CLEAR Button to reset the input fields and status bar. (If needed)

NOTE: Recommended to keep INPUT and OUTPUT Folder different for your ease to differentiate between Optimized and Unoptimized Images.
NOTE: Directory Structure in INPUT and OUTPUT Folders may differ but all Supported Images will be saved according to their directories."""
        )
    def show_about(self):
        messagebox.showinfo("Compresssio v2.0.0",
            """Compresssio is an Image Compressor which uses TinyPNG's lossy compression to compress JPG/JPEG/PNG images. 
Created and Managed by Dhruv Panchal & Urvesh Patel.
https://github.com/dhhruv
            """)

    def stop_callback(self):
        if not self.stopFlag:
            self.stopFlag = True 
            self.stop = threading.Thread(target=self.stop_execute, name="Stopping_Thread", daemon = True)
            self.stop.start()

    def stop_execute(self):
        self.stop_btn['text'] = "STOPPING..." # Set button text to stoping.
        self._status.set("Stopping the Compression. Please Wait...")
        self.status_label.update()
        
        while self.stopFlag:
            time.sleep(1)

        self.stop_btn['text'] = "STOP"
        self._status.set("Compression Cancelled!!")
        self.status_label.update()
        self.enable()
        messagebox.showinfo("Compresssio","Compression Cancelled!!")

    def compress_callback(self):
        self.disable()
        self.compress = threading.Thread(target=self.compress_execute, name="Compression_Thread", daemon = True)
        self.compress.start()

    def compress_execute(self):
        try:

            tinify.key = self._api_key.get()
            tinify.validate()
            
            if not create_dirs(self._folder_url1.get(), self._folder_url2.get()):
                return

            self._status.set("Calculating Raw Images...")
            self.status_label.update()
            
            self.raw_images = get_raw_images(self._folder_url1.get())

            if not self.raw_images:
                self._status.set("No images found within supported formats!!!")
                self.status_label.update()
                messagebox.showinfo("Compresssio","No images found within supported formats. Please check the INPUT Folder and Try Again!!!")
                self.reset_callback()
            else:
                self._status.set("Compression in Progress....")
                self.status_label.update()
                length = len(self.raw_images)
                for index,image in enumerate(self.raw_images):
                    if self.stopFlag:
                        self.stopFlag = False
                        return
                    
                    only_image_path, image_info = os.path.split(image)
                    self._status.set(f'Compressing Image [{index+1}/{length}] : {image_info}')
                    self.status_label.update()
                    change_dir(image, self._folder_url1.get(),self._folder_url2.get())
                    compress_and_save(image)
                self._status.set("Compression Completed !!")
                self.status_label.update()
                self.stopFlag = False
                self.enable()
                messagebox.showinfo("Compresssio","Compression Completed !!")
            
        except tinify.AccountError:
            messagebox.showinfo(
                "AccountError", "Please verify your Tinify API key and account limit...")
        except tinify.ClientError:
            messagebox.showinfo(
                "ClientError", "Please check your source images...")
        except tinify.ServerError:
            messagebox.showinfo("ServerError", """Temporary issue with the Tinify API. 
            	Please try again later...""")
        except tinify.ConnectionError:
            messagebox.showinfo("ConnectionError", """A network connection error occurred. 
            	Please check your Internet Connection and Try again...""")
        except Exception as e:
            messagebox.showinfo(
                "UnknownError", "Something went wrong. Please try again later...")
        self.enable()

    def reset_callback(self):
        self._folder_url1.set("")
        self._folder_url2.set("")
        self._status.set("---")
        self.stopFlag = False

bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
path_to_ico = os.path.abspath(os.path.join(bundle_dir, './files/compresssio.ico'))
ROOT = tk.Tk()
ROOT.resizable(height = False, width = False)
folder_path_1 = StringVar()
folder_path_2 = StringVar()
MAIN_WINDOW = MainWindow(ROOT)
ROOT.iconbitmap(path_to_ico)
ROOT.mainloop()