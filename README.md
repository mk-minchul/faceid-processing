b# preparing_data
Face Data preparation process to train a model for deep learning face recognition system
renamer.py - module to rename names of images in our dataset folder (format: Name_Surname_0001.png, Name_Surname_0002.png, etc.)
This format is LFW dataset format, pls follow it's instruction

----- ADDITIONAL NOTES -----

1. Collect dataset => refine, delete non-people images
- python3 removeNonFolder.py --data-dir training
2. Maybe you need to crop faces from images by using MTCNN or Retinaface
3. Refine folder names and images => renamer.py this module renames folder names of each person: it merges all the letters, removing special characters (.,-, etc) and splits the remaining string into two parts in the middle with underline '_' (rename image names according to LFW dataset format) for example: the folder A_B/A_B_0001.jpg, A_B/A_B_0002.jpg,...
- python3 renameFolder2lwfFormat.py --data-dir training
4. Align faces with - align_dataset_mtcnn_v1.py 
- python3 align_dataset_mtcnn_v1.py --data-dir training --output-dir training_processed
5. Divide into Train (80), Valid (10), Test (10) - train_valid.py and train_test.py the remaining data will be your train set
- python3 train_valid.py --data-dir training --target-dir validation
- python3 train_test.py --data-dir training --target-dir testing
6. create .lst by using im2rec.py with --list and --recursive
- python3 im2rec.py --prefix train --root training --list --recursive
7. create .rec, .idx by using im2rec.py
- python3 im2rec.py --prefix train --root training --recursive
8. create pairs.txt file using gen_pairs_lfw.py => if you don't have loop in generate() function you have to write it with range(10), because you have to create 10-folds cross validation .bin (UPD: for this you have to use your validation(verification) set)
- python3 gen_pairs_lfw.py --data-dir training/ --txt-file train_pairs.txt
9. create .bin file using dataset2bin.py
- mv train_pairs.txt training/
- python3 dataset2bin.py --data-dir training/ --file-pairs train_pairs.txt --output train.bin
10. generate property if it's neccessery
- python3 gen_property.py --data-dir training
11. Start training with insightface

## Training
python3 im2rec.py --prefix train --root training/ --list --recursive </br>
python3 im2rec.py --prefix train --root training/ --recursive </br>
python3 gen_pairs_lfw.py --data-dir training/ --txt-file train_pairs.txt
mv train_pairs.txt training/ </br>
python3 dataset2bin.py --data-dir training/ --file-pairs train_pairs.txt --output train.bin </br>

## Validation
python3 im2rec.py --prefix vald --root validation/ --list --recursive </br>
python3 im2rec.py --prefix vald --root validation/ --recursive </br>
python3 gen_pairs_lfw.py --data-dir validation/ --txt-file vald_pairs.txt </br>
mv vald_pairs.txt validation/ </br>
python3 dataset2bin.py --data-dir validation/ --file-pairs vald_pairs.txt --output vald.bin </br>

## Testing
python3 im2rec.py --prefix test --root testing/ --list --recursive </br>
python3 im2rec.py --prefix test --root testing/ --recursive </br>
python3 gen_pairs_lfw.py --data-dir testing/ --txt-file test_pairs.txt </br>
mv test_pairs.txt testing/ </br>
python3 dataset2bin.py --data-dir testing/ --file-pairs test_pairs.txt --output test.bin </br>

