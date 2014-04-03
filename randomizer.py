#!/usr/bin/python
############################################
# Name: randomizer.py                      #
# Autor: Ondrej Vavro                      #
# Description: Randomly selects specified  #
# number of images from the provided video #
# file(s).                                 #
# Date of last modification: 3 April 2014  #
############################################

import sys, os, re, argparse, cv2, random

def main():
	parser = argparse.ArgumentParser(description='Randomly selects specified number of images from provided video files.')
	parser.add_argument('video_file', nargs='+', help='Video file to be processed.')
	parser.add_argument('-n', '--num', nargs='?', default='1', type=int, help='Number of images to be extracted. (default is 1)')
	parser.add_argument('-o', '--outname', nargs='?', default="IMG_", help='Prefix of the output image files. (default is "IMG_")')
	args = parser.parse_args()

	cntvid = len(args.video_file)
	
    
    # 1) compute how many images you want from single file (using the provided number of images and the number of video files) -> CHOSEN
    # 2) or, randomly choose a number (0 to provided num of images) and after selecting (randomly) this amount of images from a random (?) video continue on other videos similarly, until all required images are selected
    # 3) or, randomly choose a number from computed range (related to provided number of images and number of video files + precision constant) and select that number of images from a video file (random?), proceed like this further 
    c=0
	while (cntvid >= 0):
	    vfile = args.video_file.pop(random.randint(0, cntvid))
		video = cv2.VideoCapture(vfile)
		cframe = video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)

		for im in range(0,int(args.num/cntvid)): # randomize the selected number of images?
			video.set(cv2.cv.CV_CAP_PROP_FRAME_COUNT,random.randint(0, cframe))
			ret, image = video.read()
			cv2.imwrite("%(name)s%(count)d.jpg" % {"name": args.outname, "count": c}, image)
			c+=1
		
		video.release()        
        cntvid -= 1

	return	# main()

if __name__ == "__main__":
	main()
