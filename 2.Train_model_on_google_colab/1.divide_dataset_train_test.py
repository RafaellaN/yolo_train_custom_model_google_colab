#This gets 10% of images and sets them as test images
#rneofy@gmail.com
import glob, os
import re
import string
import shutil
import random

# Current directory
current_dir = os.getcwd() 
print(current_dir)
image_dir=current_dir.replace("2.Train_model_on_google_colab", "1.Annotate_Images\data", 1)
print ("Image dir",image_dir)

# Copy files from 1. annotate to data for colab
dst_dir = current_dir + "\data_for_colab\data"
for filename in os.listdir(image_dir):
	filename = image_dir + "\\"+ filename
	shutil.copy(filename, dst_dir)

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
train_text_dir = current_dir + r"\data_for_colab\train_local.txt"
test_text_dir = current_dir + r"\data_for_colab\test_local.txt"
file_train = open(train_text_dir, 'w')
file_test = open(test_text_dir, 'w')
count = 0
for filename in os.listdir(dst_dir):
	if filename.endswith(".jpg"):
		count = count + 1
	
# Populate train.txt and test.txt
counter = 0


index_test = round(count / percentage_test)
print(index_test)

x = 0
# empty list
my_random_list =[];
while ( x  < index_test) :

	#my_random_list[x] = random.randint(0, count)
	my_random_list.append( random.randint(0, count))
	print("number: ", x,"random: ", my_random_list[x])
	x += 1

for filename in os.listdir(dst_dir):
	if filename.endswith(".jpg"):
		
		if counter in my_random_list:
			file_test.write(current_dir + "\data_for_colab\data\\" + filename + "\n")
		else:
			file_train.write(current_dir + "\data_for_colab\data\\" + filename + "\n")
		counter = counter + 1
