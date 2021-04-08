#This gets 10% of images and sets them as test images
#Rafaella N.
import glob, os
import re
import string

# Current directory
current_dir = os.getcwd() 

train_text_dir_local = current_dir + r"\data_for_colab\train_local.txt"
test_text_dir_local = current_dir + r"\data_for_colab\test_local.txt"

train_text_dir_colab = current_dir + r"\data_for_colab\train.txt"
test_text_dir_colab = current_dir + r"\data_for_colab\test.txt"

file_train_in = open(train_text_dir_local, 'r')
file_test_in = open(test_text_dir_local, 'r')

file_train_out = open(train_text_dir_colab, 'w')
file_test_out = open(test_text_dir_colab, 'w')

for line in file_train_in:
	file_train_out.write(line.replace(current_dir, '/content/darknet').replace('\\', '/'))

for line in file_test_in:
	file_test_out.write(line.replace(current_dir, '/content/darknet').replace('\\', '/'))




file_train_in.close()
file_train_out.close()