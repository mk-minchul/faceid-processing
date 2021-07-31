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
parser.add_argument('--data-dir', default='', help='Folder for generate property')

args = parser.parse_args()
data_dir = args.data_dir

folders = [x for x in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, x))]

n_class = len(folders)
class_0_path = os.path.join(data_dir, folders[0])
image_0 = os.listdir(class_0_path)
image = os.path.join(class_0_path, image_0[0])
h,w,c = cv2.imread(image).shape

f = open('./property', 'w')
f.write(f'{n_class},{h},{w}')
f.close()