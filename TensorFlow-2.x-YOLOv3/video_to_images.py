import cv2
vidcap = cv2.VideoCapture('Test_Video/people_walking.mp4')
success,image = vidcap.read()
count = 0
while success:
	cv2.imwrite("video_frames/frame %d.jpg" % count, image)     # save frame as JPEG file      
	success,image = vidcap.read()
	count += 1
	print('Read frame: ', count)