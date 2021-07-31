import os
import cv2
import pathlib
import argparse
# from subprocess import check_output
#print(check_output(["ls", "../input"]))
from time import time
from time import sleep
import random
import shutil
import math

# arguments to pass in command line 
parser = argparse.ArgumentParser(description='Rename images in the folder according to LFW format: Name_Surname_0001.jpg, Name_Surname_0002.jpg, etc.')
parser.add_argument('--data-dir', default='', help='dataset')

args = parser.parse_args()
data_dir = args.data_dir

folders = [x for x in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, x))]

cnt = 0
for folder in folders:
    fullPath = os.path.join(data_dir, folder)
    cnt += len(os.listdir(fullPath))

print(f'length of images: {cnt}')