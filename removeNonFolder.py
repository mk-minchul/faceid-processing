import os
import pathlib
import random
import argparse
import shutil
parser = argparse.ArgumentParser(description='Rename folders containing collected data according to => Name_Surname => formatting')
# general
parser.add_argument('--data-dir', default='', help='full path to the directory with collected images without formatting of folder names')
args = parser.parse_args()
root = args.data_dir

listdir = os.listdir(root)
for folder in listdir:
    fullPath = os.path.join(root, folder)
    try:
        listImages = os.listdir(fullPath)
        if len(listImages) == 0:
            print(f'empty folder {fullPath}')
            shutil.rmtree(fullPath, ignore_errors=True)
    except:
        continue