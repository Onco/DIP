#!/usr/bin/python
############################################
# Name: randomizer.py                      #
# Autor: Ondrej Vavro                      #
# Description: Randomly selects specified  #
# number of images from the provided video #
# file.                                    #
# Date of last modification: 6 March 2014  #
############################################

import sys, os, re, argparse#, cv2

def main():
	parser = argparse.ArgumentParser(description='Randomly selects specified number of images from a provided video file.')
	parser.add_argument('video_file', nargs=1, help='Video file to be processed.')
	parser.add_argument('-n', '--num', nargs=1, default='1', type=int, help='Number of images to be extracted. (default is 1)')
	args = parser.parse_args()

	print options
	print args

	#video = cv2.VideoCapture(video_file)
	
	#while()
	return	# main()

if __name__ == "__main__":
	main()
