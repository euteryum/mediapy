"""
################################################################################################################
################################################################################################################
## REFERENCE  :  https://truemansworld.blogspot.com/2021/04/gta-iii-trailer-maker.html
##               https://stackoverflow.com/questions/5585872/python-image-frames-to-video
##               https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python
## AUTHOR     :  euteryu
## Created on :  18/04/21
################################################################################################################
## (venv)  ==>  C:\Users\minse\Desktop\Python_misc\python-virtual-environments\Movie\Scripts\activate.bat
################################################################################################################
################################################################################################################
"""

import os
from pathlib import Path
import cv2

from mediapy.tools import makeDirectory, osPathSplitHelper
# import image.convertToHearts    ## Used in combineModifyFrames()


class Frames:
	def __init__(self, pathInput, pathOutput):
		self.pathInput  = pathInput
		self.pathOutput = pathOutput
		self.parentDirInput, self.filenameImg, self.imgExtInput    = osPathSplitHelper(pathInput)
		self.parentDirOutput, self.filenameVid, self.vidExtOutput = osPathSplitHelper(pathOutput)

	def extractFrames(self):
		vidcap        = cv2.VideoCapture(self.pathInput)
		fps           = vidcap.get(cv2.CAP_PROP_FPS)
		success,image = vidcap.read()

		count = 0
		while success:
			count += 1    #1-indexed i.e. frame1.jpg, frame2.jpg, ...
			frame = f"{self.filenameImg}{count}{self.vidExtOutput}"
			pathToFrame = os.path.join(self.parentDirOutput, frame)
			cv2.imwrite(pathToFrame, image) 
			success,image = vidcap.read()

		print(f"Frames per second  :  {fps}")
		print(f"{count} frames read.")
		print(f"Frames extracted to:  {self.parentDirOutput}")


	def combineFrames(self, fps=60):
		validImages = [img for img in os.listdir(self.dirIn) if img.endswith(f'.{self.imgExtInput}')]

		##DEBUGGING
		print("DEBUGGING: NO. OF IMAGES:  %s" % len(validImages))

		## %1d necessary for incrementing in ffmpeg command below
		## e.g.  frame1.jpg, frame2.jpg, frame3.jpg, ...
		frames     = self.filenameImg + "%01d" + self.imgExtInput
		pathToImgs = os.path.join(self.parentDirInput, frames)

		## NOTE: No FileNotFoundError shall be thrown after all
		## I assume this is due to ffmpeg msg. not quite being a Python exception
		try:
			## image2 := image file demuxer
			conversionCmd = rf'ffmpeg -f image2 -r {fps} -i {pathToImgs} -c:v mpeg4 -y {self.pathOutput}'
			os.system(conversionCmd)
		except Exception as e:
			print(e)
		else:
			print(f"Frames per second  :  {fps}")
			print(f"Movie created at   :  {self.parentDirOutput}")

	## Refactor/Rewrite combineFrames() using cv2 package in lieu of ffmpeg; then we can integrate convertToHearts()
	# def combineModifyFrames(self, fps=60):
	# 	return


############################################################################################################
############################################################################################################
## main() shows a suitable usage as a terminal-program.
## External modules should directly call the functions above instead
def main():
	print("Calling main()")
	homeDir      = str(Path.home())
	absBaseDir   = os.path.join(homeDir, 'Videos')               #HARD-CODED BASE PATH!!

	relInputDir  = input("Input directory   (may be left blank):  ")
	relOutputDir = input("Output directory  (may be left blank):  ")
	dirIn       = os.path.join(absBaseDir, relInputDir)
	dirOut      = os.path.join(absBaseDir, relOutputDir)
	makeDirectory(dirOut)

	filenameImg   = input("File name  (excl. extension)         :  ")
	imgExtInput   = input("File extension type                  :  ")
	chosenFileExt = input("Choose file extension for output     :  ")

	pathInput = os.path.join(dirIn, filenameImg + "." + imgExtInput)

	fileInput = Frames(pathInput, pathOutput)

	mode = input("Extract [e] or Combine [c]?  (Type appropriate letter):  ")
	if mode == 'e':
		return fileInput.extractFrames(self)
	elif mode == 'c':
		fps = input("Frames per second:  ")
		return fileInput.combineFrames(self, fps)
	else:
		msg = "Mode non-existent!"
		return ppError(msg)


if __name__ == "__main__":
	main()


## EXAMPLE
'''
relInputDir  ==>  3_sec
file         ==>  3_sec_video.avi
mode         ==>  'e'
'''