import cv2
import numpy as np

cap = cv2.VideoCapture(1)		  # showing camera feed
back = cv2.imread('.//image.jpg') # for background image

while cap.isOpened():
	ret, frame = cap.read()
	if ret:
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		# [H-10, 100, 100] and [H+10, 255, 255] in BGR
		
		l_blue = np.array([90, 100, 100])		# lower bound of color to change to background
		u_blue = np.array([255, 255, 255])	# upper bound for color to change to background
		
		mask = cv2.inRange(hsv, l_blue, u_blue)
		
		part1 = cv2.bitwise_and(back, back, mask = mask) # show background
		
		mask = cv2.bitwise_not(mask); # parts not marked

		part2 = cv2.bitwise_and(frame, frame, mask = mask) # show video feed

		cv2.imshow('final', part1 + part2);		# show video feed and background if there is blue are
				
		if cv2.waitKey(5) == ord('q'):			
			break

cap.release()
cv2.destroyAllWindows()