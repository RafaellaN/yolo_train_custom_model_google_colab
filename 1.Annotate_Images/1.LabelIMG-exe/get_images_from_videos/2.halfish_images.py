import cv2
import os
import glob
import shutil
import os

directory = os.getcwd() + r'\images_from_videos'
dst_dir = os.getcwd() + r'\halfish_images'
it = 0
for filename in os.listdir(directory) :
	if filename.endswith(".jpg") :
		it = it + 1 
		if not(it%20):
			print (filename, it)
			filename = directory + r"\\" + filename
			shutil.copy(filename, dst_dir)
	else:
		continue
		
		

  
  
 


