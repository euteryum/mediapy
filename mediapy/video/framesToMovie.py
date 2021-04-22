'''
C:\\Users\\minse\\Desktop\\Scripts\\framesToMovie.py

Improvements:
-- Refactor for-loop (memory-inefficient size variable!!!)
'''

import cv2
import numpy as np
from pathlib import Path
import os

import image.convertToHearts


def framesToMovie(parentDir, imgExt, vidName, fps=30):
    img_array = []
    size = 0    # dummy value

    for file in os.listdir(parentDir):
        if file.endswith(f".{imgExt}"):
            print(f"file:  {file}")
            pathToFrame = os.path.join(parentDir, file)
            img = cv2.imread(pathToFrame)
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)
        else:
            print(f"Error: file does not end with:  {imgExt}")

    print(f"Size:  {size}")

    pathToVid = os.path.join(parentDir, vidName + '.avi')
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    ## VideoWriter(file_path, fourcc, fps, (w, h))
    out = cv2.VideoWriter(pathToVid, fourcc, fps, size)
     
    for i in range(len(img_array)):
        out.write(img_array[i])

    print(f"{vidName}.avi created at:  {parentDir}")
    out.release()


def main():
    homeDir = str(Path.home())
    parentDir = os.path.join(homeDir, 'Videos\\3_sec')
    imgExt = 'jpg'
    vidName = '3_sec_video'
    framesToMovie(parentDir,imgExt, vidName)

if __name__=="__main__":
    main()