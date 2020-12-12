import os
import shutil
import sys
import tinify

SUPPORTED_FORMATS = ('jpg', 'jpeg', 'png')

def create_dirs(raw_images_dir,save_dir):

    if not os.path.isdir(raw_images_dir):
        os.makedirs(raw_images_dir)

    custom_dirs = []
    for root, directories, files in os.walk(raw_images_dir):
        for directory in directories:
            custom_path = os.path.join(save_dir, directory)
            custom_dirs.append(custom_path)

    compress_dirs = (save_dir, (*custom_dirs))
    for dir_ in compress_dirs:
        if not os.path.isdir(dir_):
            os.makedirs(dir_)

def get_raw_images(raw_images_dir):

    raw_images = []

    for root, directories, files in os.walk(raw_images_dir):
        for filename in files:
            if not filename.startswith('.'):
                file_type = filename.split('.')[-1]
                if file_type in SUPPORTED_FORMATS:
                    filepath = os.path.join(root, filename)
                    raw_images.append(filepath)

    if not raw_images:
        try:
            raise OSError('No images found within supported formats!!!')
        except OSError:
            dir_name = os.path.basename(raw_images_dir)
            sys.exit()

    return raw_images

def change_dir(abs_image_path,raw_images_dir,save_dir):

    if os.path.dirname(abs_image_path) == raw_images_dir:
        os.chdir(save_dir)

    else:
        custom_dir_path = os.path.dirname(abs_image_path)
        custom_dir_name = os.path.basename(custom_dir_path)
        compressed_custom_dir_path = os.path.join(save_dir, custom_dir_name)
        os.chdir(compressed_custom_dir_path)

def compress_and_save(abs_image_path):

    only_image_path, image_info = os.path.split(abs_image_path)
    image_name, image_type = image_info.split('.')
  
    optimized_filename = f'{image_name}_optimized.{image_type}'
    if not os.path.isfile(optimized_filename):
        source = tinify.from_file(abs_image_path)
        source.to_file(optimized_filename)

