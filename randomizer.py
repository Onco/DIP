#!/usr/bin/python
############################################
# Name: randomizer.py                      #
# Autor: Ondrej Vavro                      #
# Description: Randomly selects specified  #
# number of images from the provided video #
# file.                                    #
# Date of last modification: 6 March 2014  #
############################################

<<<<<<< HEAD
=======
import sys, os, re, argparse, cv2
>>>>>>> e375cca5ba7dc91795d766e9b6fe8c9edd58cd29

def main():
	parser = argparse.ArgumentParser(description='Randomly selects specified number of images from a provided video file.')
	parser.add_argument('video_file')
	parser.add_argument('-n', '--num', nargs='?', const='1', default='1', type='int')
	
	return	# main()

if __name__ = "__main__":
	main()
