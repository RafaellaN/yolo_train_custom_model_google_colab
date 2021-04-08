#This is for yolov3 training you have to make sure that there are no pictures without annotations

import cv2
import os
import glob
import shutil
import os
import re

image_directory = os.getcwd()+ r'\1.LabelIMG-exe\images'
label_directory = os.getcwd()+ r'\1.LabelIMG-exe\annotations'
dst_dir = os.getcwd()+ r'\data'

print(image_directory)
print(label_directory)
print(dst_dir)

for filename in os.listdir(label_directory) :

	label_filename_without_suffix = os.path.splitext(filename)[0]
	label_filename = filename
	for filename in os.listdir(image_directory) :
		image_filename_without_suffix = os.path.splitext(filename)[0]
		
		
		if (image_filename_without_suffix == label_filename_without_suffix):
			print("The filename is: ",filename)
			
			imge_to_copy_dir = image_directory + r"\\"+ filename
			label_to_copy_dir = label_directory + r"\\"+ label_filename
			print("The filename is:",imge_to_copy_dir)
			shutil.copy(imge_to_copy_dir, dst_dir)
			shutil.copy(label_to_copy_dir, dst_dir)
		
