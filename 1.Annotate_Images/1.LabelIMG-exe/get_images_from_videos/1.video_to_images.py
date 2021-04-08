import cv2
import os

video_directory = os.getcwd()+ r'\videos'
print("Video directory: ", video_directory)
for filename in os.listdir(video_directory):
	if filename.endswith(".mp4"):
		print(filename)
		#videoName = filename
		
		vidcap = cv2.VideoCapture(video_directory + r"\\" + filename)
		print(vidcap)
		success,image = vidcap.read()
		count = 0
		print(success)
		while success:
			frame_title = "images_from_videos/" + os.path.splitext(filename)[0] +"_frame" + str(count) + ".jpg"
			cv2.imwrite(frame_title, image)     # save frame as JPEG file      
			success,image = vidcap.read()
			print('Read a new frame: ', success)
			count += 1
	else:
		print("No other videos")
		continue
		

  
  
 


