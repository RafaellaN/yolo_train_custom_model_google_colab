#**YOLO GUIDE FOR CUSTOM MODEL ON WINDOWS Using google colab**
# A folder structure for future training of custom models through google colab with some python scripts that could help automate processes. Steps to do so from beginning to end.
## Requirements
### - Install Python, PyQt5 and install lxml.

## STEP 1 1.Annotate_images:
###-Download labelimg-
#### Follow this https://github.com/tzutalin/labelImg
### After you download & clicked on .exe file,remember to click on the VOC button for changing to YOLO formating
### Enable automatic saving view->auto saving
### Place all the images you want to annotate in the images directory and open it through Open dir
### Images can be taken from videos. You can transform videos to images through get_images_from_videos folder. 
### Choose Saving dir the annotations directory in the 1.labelimg
### Change the classes(custom) on the 1/Annotate_images/data/predefined_classes.txt
### Create a rect box around the object-> click next
### If the images are finished. 
### Run the "2.remove_images_without_annotation.py" all the usable images& labels will be stored to the <your_dir>/1.Annotate_Images/data 
### Now it's time to divide your dataset to train/test images. Go to folder 2.Train_model_on_google_colab
##
## STEP 2 2.Train_model_on_google_colab:
### Now we want to divide the pictures to train/ test. To do so run 1.divide_dataset_train_test.py
### Run the 1.divide_dataset_train_test.py this will divide the images in the data_for_colab folder (train_local.txt, test_local.txt)
### We have to calculate and replace anchors. Run 2.anchors.py. If everything is correct until now it will generate a anchors6.txt file in the 2.anchors folder
### Anchor is like a default bounding box for a cell. It is composed of width and height for each anchor.
### Compress the data_for_colab and you are done with annotating
### https://colab.research.google.com/ 