import os
import time
from PIL import Image

# ------------
# --- Constants
# ------------

# Input and Output folders
INPUT_FOLDER = "convert"
OUTPUT_FOLDER = "output"

# File extensions
IMAGE_EXTENSIONS = ["jfif", "jpg", "png", "jpeg", "tif", "tiff"]
MOVE_ALL = False
# -----------
# --- Functions
# -----------
def move_file(infile):
    """
    Moves a file from one location to another
    """
    try:
        os.rename(INPUT_FOLDER + "/" + infile, OUTPUT_FOLDER + "/" + infile)
    except FileExistsError:
        print("File already exists\n")

def convert_file_extension(file_name, lossless, quality):
    """
    Converts a file with a given extension to png/jpg
    """
    global MOVE_ALL
    file_extension = "png"
    # check if file is png and lossless is true, if so, convert skip
    if lossless and ".png" in file_name:
        print("Skipping" + file_name + " because it's already lossless\n")
        if MOVE_ALL:
            move_file(file_name)
            return
        
        mv = input("Would you like to move " + file_name + " to output? (Y/N/ALL): ")
        if mv.lower() == "y" or mv.lower() == "all":
            print("Moving " + file_name + " to output")
            move_file(file_name)
        elif mv.lower() == "all":
            MOVE_ALL = True
        return
    if not lossless:
        file_extension = "jpg"
    # Create output file name
    output_file_name = file_name.split(".")[0] + "." + file_extension

    # Open file
    im = Image.open(INPUT_FOLDER + "/" + file_name)
    if not lossless:
            im = im.convert('RGB')
            im.save(OUTPUT_FOLDER + "/" + output_file_name, quality=quality)
    else:
        im.save(OUTPUT_FOLDER + "/" + output_file_name, "PNG")
    

    

def convert_files(lossless, quality):
    """
    Converts all files with a given extension to png
    """
    for file in os.listdir(INPUT_FOLDER):
        file_name, file_extension = file.split(".")

        # Check if file is a supported image file
        if file_extension.lower() in IMAGE_EXTENSIONS:
            convert_file_extension(file, lossless, quality)

# ------------
# --- Main
# ------------

if __name__ == "__main__":
    # Create output folder if it does not exist
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Start time
    start_time = time.time()

    # Asks user if he wants to convert all files in the input folder to lossless png or lossy jpg
    loss = input("Lossless or lossy (default: Lossless): ")
    loss = loss.lower()
    while loss != "lossless" and loss != "lossy" and loss != "":
        print("Invalid argument.\n")
        loss = input("Lossless or lossy (default: Lossless): ")
    if loss == "lossy":
        quality = int(input("Quality (default: 100):"))
        while quality > 100 or quality < 0:
            print("Invalid quality integer.\n")
            quality = int(input("Quality (default: 100): "))
        print(f"Converting to lossy files with quality({quality})")
        convert_files(lossless=False, quality=quality)
    else:
        print("Converting to lossless png files\n")
        convert_files(lossless=True, quality=100)

    # End time
    end_time = time.time()


    # Print time
    print("Converted all files in " + str(round(end_time - start_time, 2)) + "s")