import os
import pathlib
import random
import argparse

parser = argparse.ArgumentParser(description='Rename folders containing collected data according to => Name_Surname => formatting')

parser.add_argument('--data-dir', default='', help='full path to the directory with collected images without formatting of folder names')
args = parser.parse_args()
root = args.data_dir

for path, subdirs, files in os.walk(root):
    for subdir in subdirs:
        if len(subdir.split("_")) != 2:
            previousName = subdir
            subdir += f'_temp{random.randint(0,1000000000)}'
            src = os.path.join(path, previousName)
            des = os.path.join(path, subdir)
            print(f'src {src}, des {des}')
            os.rename(src, des)

for path, subdirs, files in os.walk(root):
    i = 1
    print("filles: ", files)
    for name in files:
        extension = name.split(".")[-1].lower()
        if extension not in ["jpg", "png", "jpeg"]:
            continue
        print(f'name: {name}')
        stri = str(random.randint(1,1000))
        stri = stri.zfill(4)
        print(f'stri {stri}')
        src = os.path.join(path, name)
        des = os.path.join(path, os.path.basename(path) + "_" + stri + '.' + extension)
        print(f'source: {src}, destination: {des}')
        os.rename(src, des)
        i = i + 1
        print(os.path.basename(path))
