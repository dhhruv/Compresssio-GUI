#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import os.path
from tkinter import messagebox
import shutil
import sys
import tinify

SUPPORTED_FORMATS = ("jpg", "jpeg", "png")


def create_dirs(raw_images, save_dir):
    for image in raw_images:
        compress_dir = save_dir + "/" + os.path.dirname(image)
        if not os.path.isdir(compress_dir):
            os.makedirs(compress_dir)


def get_raw_images(raw_images_dir):

    if not os.path.isdir(raw_images_dir):
        messagebox.showinfo(
            "Directory Error !",
            """Input Folder Does not Exist.
        Please Check the Directory and Try Again""",
        )

    raw_images = []

    for (root, directories, files) in os.walk(raw_images_dir):
        for filename in files:
            if not filename.startswith("."):
                file_type = filename.split(".")[-1].lower()
                if file_type in SUPPORTED_FORMATS:
                    filepath = os.path.join(root, filename)
                    raw_images.append(filepath.replace(raw_images_dir, ""))

    return raw_images


def change_dir(abs_image_path, raw_images_dir, save_dir):
    custom_dir_path = os.path.dirname(abs_image_path)
    custom_dir_path = custom_dir_path.split("\\")
    compressed_custom_dir_path = save_dir + "/" + "/".join(custom_dir_path)
    os.chdir(compressed_custom_dir_path)


def compress_and_save(abs_image_path):

    (only_image_path, image_info) = os.path.split(abs_image_path)

    index = image_info.rindex(".")
    (image_name, image_type) = (image_info[:index], image_info[index + 1 :])
    optimized_filename = "{}_optimized.{}".format(image_name, image_type)
    if not os.path.isfile(optimized_filename):
        source = tinify.from_file(abs_image_path)
        source.to_file(optimized_filename)
