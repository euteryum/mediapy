################################################################################################################
################################################################################################################
## REFERENCE  :  ./
## AUTHOR     :  euteryu
## Created on :  20/12/20
################################################################################################################
## (venv)  ==>  C:\Users\minse\Desktop\Python_misc\python-virtual-environments\love\Scripts\activate.bat
################################################################################################################
################################################################################################################

from PIL import Image, ImageDraw, ImageFilter
import os

'''
PLAN:
0) https://packaging.python.org/tutorials/packaging-projects/
1) OVERLOAD CONVERSION METHODS, DEPENDING ON PARAMETERS
2) CREATE PRIVATE FUNCTION  <==  DRY PRINCIPLE, ABSTRACT LOGIC
'''

def convertToHeartFramed(pathInput, pathOutput):
	self.parentDirInput, self.filenameImg, self.imgExtInput = osPathSplitHelper(pathInput)

    rel_path_input = inputFile
    rel_path_alpha = 'heart_alpha.jpg'     # ?? Is this the overlay image

    im_rgb = Image.open(os.path.join(src_dir, rel_path_input))
    im_a = Image.open(os.path.join(src_dir, rel_path_alpha)).convert('L').resize(im_rgb.size)

    im_rgba = im_rgb.copy()
    im_rgba.putalpha(im_a)
    im_rgba.save(os.path.join(dst_dir, 'alpha' + rel_path_input))


# TESTING
def main():
    src_dir = r'C:\Users\minse\Pictures\Love'
    dst_dir = r'C:\Users\minse\Pictures\Love\thumbnails'
	inputFile = 'beach1.png'
	pathInput
	convertToHeartFramed(pathInput)

if __name__=="__main__":
	main()