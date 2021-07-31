import os
import shutil



path = '/mnt/Downloads/azure_storage/hmt-dev-ai-model/celebrity/'
current_folder = './celebrity_copy_2'
listdir = os.listdir(path)

copyFolder = [(os.path.join(path, x), x) for x in listdir[:len(listdir)//1000]]
print(f'length copy folder: {len(copyFolder)}')
for folder in copyFolder:
    shutil.copytree(folder[0], os.path.join(current_folder, folder[1]))