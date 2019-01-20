#! /usr/bin/python3
import os, sys, shutil, send2trash

#-----------------------------------------------------------------------------------------------------
# SYNOPSIS:
# This program will take all the files in the current directory and rename them all sequentially.
# By default, it will do so in the order the files are encountered.
## Future features will be the same concept but per file types. So, there could be a 1.png and 1.jpg
#-----------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------
# TODO: Single # means main point, double # means sub-point
# Check if the next renaming already exists.
## Give prompt if a filename already exits and give choice of overwrite, take next name, or skip.
# Add option to specify a prefix to the filename. Example: catgirl1.png or foxgirl001.png
#-----------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------
# Calculates the total size of the current directory in Bytes.
# Displays the source directory and destination directory
# Requires confirmation before the program will continue.
#-----------------------------------------------------------------------
def confirmation(destfolder):
	totalSize = 0
	for file in currentDir:
		totalSize += os.path.getsize('./' + file)


	print('\nCurrent directory size: ' + str(totalSize) + ' Bytes.')
	print('Source: ' + os.getcwd() + '\nDestination: ' + os.path.abspath('./' + destFolder))
	confirmation = input("\nDo you want to continue? (y/n): ")
	if confirmation.lower() == 'n':
		sys.exit()




#-----------------------------------------------------------------------
# Prompts the user to select a name for the destination folder to be 
#	 created.
# Alternatively, if a name for a folder is chosen and already exists,
#  this function will return a tuple containing 'delete' to signal that
#  the folder will need to be deleted so a new one can be created.
#-----------------------------------------------------------------------
def folderSelect():
	while True:
		newFolder = input("Creating destination folder. Enter name: ")

		#Checks if the folder already exists
		if newFolder in os.listdir():
			if os.path.isdir('./' + newFolder):
				print("This directory already exists.")

				if input("Would you like to write to it anyway?\nWARNING: That folder will be sent to the trash! (y/n): ").lower() == 'y':
					return newFolder, 'delete'

				else:
					continue

		else:
			return newFolder, ''




#-----------------------------------------------------------------------
# Creates a folder to place the newly renamed files in.
# Deletes a pre-existing folder if the folder name the user selected
#  is already in use. (The existing folder is actually sent to trash)
#-----------------------------------------------------------------------
def folderCreate(selectTuple):
	if selectTuple[1] == 'delete':
		send2trash.send2trash('./' + selectTuple[0])

	os.makedirs('./' + selectTuple[0])
	


#-----------------------------------------------------------------------
# Moves the files to the created folder.
# The function to create the folder is called here.
# Moves only files and not directories.
#-----------------------------------------------------------------------
def moveFiles(destFolder):
	num = 0	
	for file in currentDir:
		if os.path.isdir('./' + file) == False:
			extension = os.path.splitext(file)[1]
			shutil.move(('./' + file), './' + destFolder + os.path.sep + str(num) + extension)
			num += 1





#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
currentDir = os.listdir()
selectTuple = folderSelect()
destFolder = selectTuple[0]
confirmation(destFolder)
folderCreate(selectTuple)
moveFiles(destFolder)
#
