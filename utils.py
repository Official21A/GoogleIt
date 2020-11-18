import os
import datetime


DATE_FORMAT = "%b %d %Y  %H:%M"
MAIN_DIR = "./docs/"


def utils_init():
	# To start the program by creating the main dir if needed
	print("Welcome to google it.")
	print(datetime.datetime.now().strftime(DATE_FORMAT))
	dir_check()


def dir_check():
	# Check for existance of main directory
	if not os.path.exists(MAIN_DIR):
		os.mkdir(MAIN_DIR)
