import os
import shutil
import pathlib
import argparse
import numpy as np
import pandas as pd
from time import time
from time import sleep
import random
import math



parser = argparse.ArgumentParser(description='Rename images in the folder according to LFW format: Name_Surname_0001.jpg, Name_Surname_0002.jpg, etc.')

parser.add_argument('--training', default='./training', help='Full path to the directory with peeople and their names, folder should denote the Name_Surname of the person')
parser.add_argument('--testing', default='./testing', help='Full path to the directory with peeople and their names, folder should denote the Name_Surname of the person')
parser.add_argument('--validation', default='./validation', help='Full path to the directory with peeople and their names, folder should denote the Name_Surname of the person')

args = parser.parse_args()
training = args.training
testing = args.testing
validation = args.validation

def correct(path):
    dir1 = os.listdir(path)
    dir1 = [x for x in dir1 if os.path.isdir(os.path.join(path, x))]
    return dir1

trainingFolder = correct(training)
testingFolder = correct(testing)
validationFolder = correct(validation)

print('Check testing folder')
for folder in testingFolder:
    if folder not in trainingFolder:
        print(f'{x} not in training')
        print('list:')
        print(os.listdir(os.path.join(testing, x)))
        shutil.rmtree(os.path.join(testing, x))

print('Check validation folder')
for folder in validationFolder:
    if folder not in trainingFolder:
        print(f'{x} not in training')
        print('list:')
        print(os.listdir(os.path.join(validation, x)))
        shutil.rmtree(os.path.join(validation, x))
        