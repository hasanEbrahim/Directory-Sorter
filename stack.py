import os 
import sys
import shutil 

# Take user input for the path to be sorted
user_input = input("Enter the path that you want to sort: ")
# Enter path that needs to be sorted
path = user_input

# create organized list in determined path/directory
list_ = os.listdir(path) 

# split filename and extension 
for file_ in list_: 
	name, ext = os.path.splitext(file_) 

# store the extension type 
	ext = ext[1:] 

# This forces the next iteration, 
# if it is the directory 
	if ext == '': 
		continue

# This will move the file to the directory 
# where the name 'ext' already exists 
	if os.path.exists(path+'/'+ext): shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_) 
# This will create a new directory, 
# if the directory does not already exist 
	else: 
		os.makedirs(path+'/'+ext) 
		shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_) 

# Hasan Ebrahim 2020
