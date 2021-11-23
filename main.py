import os
from PIL import Image

# get the current working directory
cwd = os.getcwd()

# get the list of files in the convert folder
convert_files = os.listdir(cwd + '/convert')

# loop through the files in the convert folder
for file in convert_files:
    # get the file name and extension
    file_name, file_ext = os.path.splitext(file)

    # if the file is a jfif file
    if file_ext == '.jfif':
        # open the image
        image = Image.open(cwd + '/convert/' + file)

        # convert the image to png
        image.save(cwd + '/output/' + file_name + '.png', 'png')