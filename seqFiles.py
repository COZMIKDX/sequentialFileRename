#! /usr/bin/python3

import os, sys, shutil, send2trash

# This program will take all the files in the current directory and rename them all sequentially.
# By default, it will do so in the order the files are encountered.
## Future features will be the same concept but per file types. So, there could be a 1.png and 1.jpg



###TODO: Single # means main point, double # means sub-point
# Check if the next renaming already exists.
# Decide if it should rename like 1.png, 2.png, 3.png, and so on or like 001.png, 002.png.
## If the latter, count the amount of files in the folder and decide the number or zeroes to use.
# Add option to specify a prefix to the filename. Example: catgirl1.png or foxgirl001.png
#Make sure this doesn't delete or overwrite anything. This include checking if a rename pre-exists.
#Give prompt if a filename already exits and give choice of overwrite, take next name, or skip.

### Outline: Ver 1.0 [Linux only]
# Get list of files in current directory.
# Iterate through it with a loop.
## Check if the name to rename the file as is already taken so you don't accidentally delete anything.
### Alternatively, place all newly renamed files in a new folder so you don't have to check.
## Rename the file.
## Move on to the next file.
#Done

#List the directory this file was called in.
currentDir = os.listdir()

def greeter():
	print("Displaying files in current directory:")
	totalSize = 0
	for file in currentDir:
		totalSize += os.path.getsize('./' + file)
		print(file)



	print('\nDirectory size: ' + str(totalSize) + ' Bytes.')
	confirmation = input("\nDo you want to continue? (y/n): ")
	if confirmation.lower() == 'n':
		sys.exit()





#called in folderCreate().
#Returns a tuple. [0] is the folder name. [1] is whether or not to delete an existing folder.
def folderSelect():
	while True:
		newFolder = input("Creating destination folder. Enter name: ")

		#Checks if the folder already exists
		if newFolder in os.listdir():
			if os.path.isdir('./' + newFolder):
				print("This directory already exists.")

				#Ask to use existing folder. Yes exits the loop with folder name. No goes back to the start of the loop.
				if input("Would you like to write to it anyway?\nWARNING: That folder will be sent to the trash! (y/n): ").lower() == 'y':
					return newFolder, 'delete'

				else:
					continue

		#The chosen folder name is available. The program will continue.
		else:
			return newFolder, ''





def folderCreate():
	#Currently may delete file with same name as directory. Untested.
	selectTuple = folderSelect()

	if selectTuple[1] == 'delete':
		send2trash.send2trash('./' + selectTuple[0])

	os.makedirs('./' + selectTuple[0])
	return selectTuple[0]
	

# [Ver 1.0]: Moves files without checking for name conflicts. 
#		The program currently creates a new folder so no filename checking is needed yet.
def moveFiles():
	destFolder = folderCreate()

	#number to name the file with.
	num = 0	
	for file in currentDir:
		#The following currently uses the separators for linux.
		if os.path.isdir('./' + file) == False:
			extension = os.path.splitext(file)[1]
			shutil.move(('./' + file), './' + destFolder + '/' + str(num) + extension)
			num += 1





###################################################################################################
greeter()
moveFiles()
#
