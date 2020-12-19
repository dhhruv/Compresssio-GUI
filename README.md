<p align="center">
  <img src="https://user-images.githubusercontent.com/72680045/102008832-56a57600-3d59-11eb-821a-98b8adabbbc9.png">
  <h2 align="center" style="margin-top: -4px !important;">Streamline/Optimize your Images to save storage space...</h2>
  <p align="center">
    <a href="https://github.com/dhhruv/Compresssio/blob/master/LICENSE">
      <img src="https://img.shields.io/github/license/dhhruv/Compresssio-GUI?color=informational">
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/python-v3.8-informational">
    </a>
    <img src="https://img.shields.io/badge/maintainer-dhhruv-informational">
    <a href="https://github.com/dhhruv/Compresssio-GUI">
    	<img src="https://img.shields.io/github/v/release/dhhruv/Compresssio-GUI">
    </a>
    <img src="https://img.shields.io/badge/contributions-welcome-informational">
  </p>
</p>

# Compresssio:

The above script uses TinyPNG's savvy lossy compression methods to reduce the document size of your JPG/PNG files. This is achieved by specifically decreasing the number of colors in the image, therefore lesser number of bytes are required to store the information. The impact of the script is nearly invisible but it makes an exceptionally enormous effect in file size of the image.

## Image Comparison:

<p align="center">
	<img src="https://user-images.githubusercontent.com/72680045/102686318-e2614b80-420c-11eb-8807-2fce966c52f7.png">
	<h4 align="center" style="margin-top: -4px !important;">Original Image (Size: 3.29 MB)  Optimized Image (Size: 1.30 MB)</h4>
</p>
<br>
<p align="center">
	<img src="https://user-images.githubusercontent.com/72680045/102686321-e42b0f00-420c-11eb-84a0-4fbb2f966b20.png">
	<h4 align="center" style="margin-top: -4px !important;">Original Image (Size: 3.80 MB)  Optimized Image (Size: 1.21 MB)</h4>
</p>
<br>

## Setup (Windows):

1. Install Python
2. Clone this repository
```
git clone https://github.com/dhhruv/Compresssio-GUI.git
```

3. Install, create and activate virtual environment.
For instance we create a virtual environment named 'venv'.
```
pip install virtualenv
python -m virtualenv venv
venv\Scripts\activate.bat
```

4. Install dependencies
```
pip install -r requirements.txt
```

<p align="center">
	<img src="https://user-images.githubusercontent.com/72680045/102009746-8a839a00-3d5f-11eb-9fee-51cecb6dd061.PNG">
</p>
<br>

## How to Get Your API Key !

You can Find your API Key from the Website [https://tinypng.com/developers](https://tinypng.com/developers) after Signing Up and save it somewhere on your PC/Laptop.


## How To Use !
1.	Click SELECT INPUT FOLDER Button to select the INPUT FOLDER which contains all the Images to be Compressed/Optimized.
2.	Click SELECT OUTPUT FOLDER Button to select the OUTPUT FOLDER which will contain all the the Compressed/Optimized Images. (After Compression)
3.	Enter Your API Key from TINYPNG Website. If you don't have one in possession then you can find on this website https://tinypng.com/developers .
4.	Hit the COMPRESS Button and the INPUT FOLDER containing Supported Image Formats will be Compressed and saved in the OUTPUT FOLDER.
5.	Click CLEAR Button to reset the input fields and status bar. (If needed)

## Important Note:

-	**The limit you'll have at first is of 500 images per month on the Free plan. You can change this according to your requirement at [https://tinypng.com/developers](https://tinypng.com/developers)**
-	**Recommended to keep INPUT and OUTPUT Folder different for your ease to differentiate between Optimized and Unoptimized Images.**
-	**This Script is just a Prototype so Metadata is not stored in the Compressed Images from the Original Images.**
-	**Directory Structure in INPUT and OUTPUT Folders may differ but all Supported Images will be saved according to their directories.**
-	**The Authors will not be responsible for any kind of loss of data so it is essential to have a Backup of Original Data placed in the Input Folder. Read the [LICENSE](https://github.com/dhhruv/Compresssio-GUI/blob/master/LICENSE) for more information.**

## Contributors:

<a href="https://github.com/dhhruv/Compresssio-GUI/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=dhhruv/Compresssio-GUI" />
</a>

