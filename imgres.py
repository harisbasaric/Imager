'''
IMPORTANT NOTE:
imgres is actually the subprogram of imager; Imager is the GUI version of imgres
'''

# Written by Haris Basaric
# imgres - Resize multiple images in one go, command line interface
# 26 November 2019

# using PIL - Python Imaging Library
from PIL import Image
import os
import sys

#imgres my_pictures_folder

# directory is the location where all photos are
# program automatically creates new directory with additional "_small"
# make system call to create new directory
directory = sys.argv[1]
new_directory = directory + "_small"
os.mkdir(new_directory)

# the process of getting the reduction percentage from user
print ("\n IMAGE RESIZER BY HARIS BASARIC \n")
percent = int(input("Please enter the % (1-99): "))
percent /= 100
print ("Ratio: " + str(percent))

# for every file in the directory
for file_name in os.listdir(directory):

    # open the file as "image"
    print("Processing %s" % file_name)
    image = Image.open(os.path.join(directory, file_name))

    # get the size of the image
    # calculate the new dimensions based on current size and user-given percentage
    # create "output" object that will be the resized original "image" object
    x,y = image.size
    new_dimensions = (round(x*percent), round(y*percent))
    output = image.resize(new_dimensions, Image.ANTIALIAS)

    # create file name variable that will have prefix "small_" that will be binded to new directory
    # save "output" image as named by the output_file_name as JPEG in new directory
    output_file_name = os.path.join(new_directory, "small_" + file_name)
    output.save(output_file_name, "JPEG", quality = 95)

# after everything is complete
print("All done")
