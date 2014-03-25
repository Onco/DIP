#!/usr/bin/python
############################################
# Name: randomizer.py                      #
# Autor: Ondrej Vavro                      #
# Description: Randomly selects specified  #
# number of images from the provided video #
# file.                                    #
# Date of last modification: 6 March 2014  #
############################################

import sys, os, re, argparse, cv2, random

def main():
	parser = argparse.ArgumentParser(description='Randomly selects specified number of images from a provided video file.')
	parser.add_argument('video_file', nargs='?', help='Video file to be processed.')
	parser.add_argument('-n', '--num', nargs='?', default='1', type=int, help='Number of images to be extracted. (default is 1)')
	parser.add_argument('-o', '--outname', nargs='?', default="IMG_", help='Prefix of the output image files. (default is "IMG_")')
	args = parser.parse_args()


	video = cv2.VideoCapture(args.video_file)
	numf = video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)

	for im in range(0,args.num):
		video.set(cv2.cv.CV_CAP_PROP_FRAME_COUNT,random.randint(0, numf))
		ret, image = video.read()
		cv2.imwrite("%(name)s%(count)d.jpg" % {"name": args.outname, "count": im}, image)
		

        video.release()        

	return	# main()

if __name__ == "__main__":
	main()
