import cv2
#print(cv2.__version__) #Prints OpenCV version

#Creates capture object, reading video from a file
vid_capture = cv2.VideoCapture('Cars.mp4')

#Returns False if error when opening video file
if (vid_capture.isOpened() == False):
  print("Error opening the video file")
else:
  print("Video opened succesfully")
  # Get frame rate information
  fps = int(vid_capture.get(cv2.CAP_PROP_FPS)) #or cv2.CAP_PROP_FPS instead of 5
  print("Frame Rate : ",fps,"frames per second")  
 
  # Get frame count
  frame_count = vid_capture.get(7) #or cv2.CAP_PROP_FRAME_COUNT instead of 5
  print("Frame count : ", frame_count)

while(vid_capture.isOpened()):
  # vCapture.read() methods returns a tuple, first element is a bool 
  # and the second is frame
 
  ret, frame = vid_capture.read()
  
  if ret == True:
    cv2.imshow('Autobahn webcam',frame)
    k = cv2.waitKey(20)
    #If you press q stop
    if k == ord('q'):
      break
  else:
    break

# Release the objects
vid_capture.release()
cv2.destroyAllWindows()