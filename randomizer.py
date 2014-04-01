#!/usr/bin/python
############################################
# Name: randomizer.py                      #
# Autor: Ondrej Vavro                      #
# Description: Randomly selects specified  #
# number of images from the provided video #
# files.                                   #
# Date of last modification: 1 April 2014  #
############################################

import sys, os, re, argparse, cv2, random

def main():
	parser = argparse.ArgumentParser(description='Randomly selects specified number of images from provided video files.')
	parser.add_argument('video_file', nargs='+', help='Video file to be processed.')
	parser.add_argument('-n', '--num', nargs='?', default='1', type=int, help='Number of images to be extracted. (default is 1)')
	parser.add_argument('-o', '--outname', nargs='?', default="IMG_", help='Prefix of the output image files. (default is "IMG_")')
	args = parser.parse_args()

	cntvid = len(args.video_file)
	c=0
    
    # select random file from input files and select random? number of images from the first file :) (perhaps random from 1st, num_of_imgs - random, random from 2nd, num_of_imgs - random, etc...)
    vfile = args.video_file.pop(random.randint(0, cntvid))	# pop gives an exception - not good
    cntvid -= 1
	while (cntvid >= 0): # use try/catch instead of counting? other function? how?
		video = cv2.VideoCapture(vfile)
		cframe = video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)

		for im in range(0,int(args.num/cntvid)):
			video.set(cv2.cv.CV_CAP_PROP_FRAME_COUNT,random.randint(0, cframe))
			ret, image = video.read()
			cv2.imwrite("%(name)s%(count)d.jpg" % {"name": args.outname, "count": c}, image)
			c+=1
		
		video.release()        
        vfile = args.video_file.pop(random.randint(0, cntvid))	# this here?
        cntvid -= 1

	return	# main()

if __name__ == "__main__":
	main()
