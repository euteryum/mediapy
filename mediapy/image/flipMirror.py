####################################################################################################
####################################################################################################
## REFERENCE  :  https://note.nkmk.me/en/python-pillow-flip-mirror/
## AUTHOR     :  euteryum
## Created on :  17/04/21
####################################################################################################
## UPDATE 18/04/21:
## -- Successfully placed my ugly, non-scalable methods into a class
## -- Hence, python-doc comments below this line DOES NOT APPLY ANY LONGER!!!
####################################################################################################
####################################################################################################
## Original thought process:
## -- We're merely making use of `ImageOps.flip()`, and it's unlikely we'll specify different imgs
##    to flip and mirror by ourselves in this TERMINAL APPLICATION - such cases should be automated
##    in a for-loop anyway!
## -- I may as well make `relativePath` global.
## -- tl;dr  This program is NOT meant to be used as an API.
####################################################################################################
## Use case:
## -- Flip and/or mirror operation on the SAME, SINGLE image file.
####################################################################################################
## Potential Improvements:
## -- Make into an API  <==  make a CLASS
####################################################################################################
####################################################################################################


from pathlib import Path
import os
from PIL import Image, ImageOps


## Utility method(s)
def makeDirectory(filePath):
	try:
		if not os.path.exists(filePath):
			os.makedirs(filePath)  #Raise error exception if leaf directory already exists or cannot be created. 
	except (IOError, OSError):
		print ('Error: Directory cannot be created! Possibly permission error?')

def openImage(filePath):
	try:
		im = Image.open(filePath)
		return im
	except FileNotFoundError:
		print ('Error: File not found! Perhaps wrong directory/filename?')


class FlipMirror:
	def __init__(self, imgFile, absSrcDir, absDstDir):
		self.img_File    = imgFile
		self.abs_Src_Dir = absSrcDir
		self.abs_Dst_Dir = absDstDir
		self.path_To_Img = os.path.join(self.abs_Src_Dir, self.img_File)
		self.img_obj     = openImage(self.path_To_Img)

	## flip (up<->down)
	def flip(self):
		im_flip = ImageOps.flip(self.img_obj)
		im_flip.save(os.path.join(self.abs_Dst_Dir, 'flipped_' + self.img_File), quality=95)
		print("Image flipped.")

	## mirror (left<->right)
	def mirror(self):
		im_mirror = ImageOps.mirror(self.img_obj)
		im_mirror.save(os.path.join(self.abs_Dst_Dir, 'mirrored_' + self.img_File), quality=95)
		print("Image mirrored.")


def main():
	# homeDir = r'C:\Users\minse\'                   #Don't use raw strings in lieu of generic path below
	homeDir      = str(Path.home())
	abs_Base_Dir   = os.path.join(homeDir, 'Pictures')

	rel_Input_Dir  = input("Input directory  (leave blank if ~/Pictures):  ")
	rel_Output_Dir = input("Output directory (leave blank if ~/Pictures):  ")
	abs_Src_Dir    = os.path.join(abs_Base_Dir, rel_Input_Dir)
	abs_Dst_Dir    = os.path.join(abs_Base_Dir, rel_Output_Dir)
	makeDirectory(abs_Dst_Dir)

	img_File      = input("Input-file name                             :  ")

	## Create image object(s) to reflect:
	image1 = FlipMirror(img_File, abs_Src_Dir, abs_Dst_Dir)
	# image1.flip()
	image1.mirror()


if __name__ == "__main__":
	main()


## EXAMPLES
'''
input("Input-directory:  ")  ==>  Love\thumbnails
input("Input-file name:  ")  ==>  beach1.png
'''