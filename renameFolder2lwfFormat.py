import os
import pathlib
import random
import argparse
import string
import shutil

parser = argparse.ArgumentParser(description='Rename folders containing collected data according to => Name_Surname => formatting')
parser.add_argument('--data-dir', default='', help='full path to the directory with collected images without formatting of folder names')
args = parser.parse_args()
root = args.data_dir

listdir = os.listdir(root)
char_set = string.ascii_uppercase + string.digits

for folder in listdir:
    if len(folder.split('_')) < 2:
        surname = ''.join(random.sample(char_set*6, 10))
        new_name = folder.split('_')[0] + '_' + surname
    else:
        continue
    src = os.path.join(root, folder)
    dst = os.path.join(root, new_name)
    shutil.move(src, dst)
    print(f'Moved folder {src} to {dst}')
