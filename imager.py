# Written by Haris Basaric
# Imager - Resize multiple images in one go
# 13 April 2020

# use PIL - Python Imaging Library, used for resizing the image and exporting the resized image
from PIL import Image
# Tkinter used for GUI
import tkinter as tk
import os
import sys

# importing specific functions for easier use
# filedialog is prompt for opening and selecting folder
# messagebox is for displaying info when process is finished
from tkinter import filedialog
from tkinter import messagebox

# defining the main window object, setting the title, and windows size
root = tk.Tk()
root.title("Imager by Haris")
root.geometry('400x100')

# function that prints to console reduction percentage and selected folder
# not used actually in the program currently, but it's useful for debugging
def show_entry_fields():
    print("Folder: %s\n Percentage: %s" % (folder_entry.get(), percentage_entry.get()))

# function calld when "Load Folder" button is pressed
# prompts file dialog where we select folder
# inserts the path to selected folder into text box
def load_folder():
    folder_selected = filedialog.askdirectory()
    folder_entry.insert(0, str(folder_selected))
    print ("Folder selected: %s" % (folder_selected))

# function that resizes every image in selected folder by reduction percentage
def resize_image():
    # gets the selected folder
    # create a new one with same name + with suffix "_small"
    # get the ratio from percentage
    directory = folder_entry.get()
    new_directory = directory + "_small"
    os.mkdir(new_directory)
    percent = int(percentage_entry.get())
    percent /= 100
    print ("Ratio: " + str(percent))

    # for every image in selected folder
    # open it
    for file_name in os.listdir(directory):
        print("Processing %s" % file_name)
        image = Image.open(os.path.join(directory, file_name))

        # get image dimensions
        # and multiply the current dimensions with given ratio
        # create new image object that will resize original image and set it to new dimensions
        x,y = image.size
        new_dimensions = (round(x*percent), round(y*percent))
        output = image.resize(new_dimensions, Image.ANTIALIAS)

        # make output file named "small_" + original file name and address it to new folder
        # save the image to that location
        output_file_name = os.path.join(new_directory, "small_" + file_name)
        output.save(output_file_name, "JPEG", quality = 95)

    # print info to console and show the message box if everything is ok
    print("All done")
    tk.messagebox.showinfo('Done', 'Operation successfully completed')

# Below are GUI elements

# Labels
tk.Label(root, text="Picutres Folder ").grid(row=0)
tk.Label(root, text="Resize percentage (%) ").grid(row=1)

# Entries / text box input fields for folder name and percentage
folder_entry = tk.Entry(root, width=40)
percentage_entry = tk.Entry(root, width=10)

# positioning entries
folder_entry.grid(row=0, column=1)
percentage_entry.grid(row=1, column=1)

# two buttons for selection of folder and Resize
# "Load Folder" triggers load_folder() fucntion
# "Resize" triggers resize_image() function
tk.Button(root, text='Load Folder', command=load_folder).grid(row=3, column=0, pady=10)
tk.Button(root, text='Resize', command=resize_image).grid(row=3, column=1, pady=10)

root.mainloop()
