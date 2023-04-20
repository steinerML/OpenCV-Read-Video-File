# OpenCV Read and Write Videos
Reading and Writing videos using OpenCV
## Contents:

Reading and writing videos in OpenCV is very similar to reading and writing images. A video is nothing but a series of images that are often referred to as frames.

I have used the following functions/methods:

| Function        |Action                                                                        |
|----------------:|------------------------------------------------------------------------------|
|cv2.VideoCapture | Creates a video capture object, which would help stream or display the video.|
|cv2.VideoWriter  | Saves the output video to a directory.                                       |
|     cv2.imshow()|  Displays image.                                                             |
|    cv2.waitKey()|  Wait for key.                                                               |
|     get()       |  Retrieves video metadata                                                    |


## Test Video used: 
Below the video we used to execute the aforementioned functions:

![Source Image](https://learnopencv.com/wp-content/uploads/2021/05/image.gif)


## Summary:

```python
#Creates capture object, reading video from a file
vid_capture = cv2.VideoCapture('Cars.mp4')
```

```python
# Get frame rate information
fps = int(vid_capture.get(cv2.CAP_PROP_FPS)) #or cv2.CAP_PROP_FPS instead of 5
print("Frame Rate : ",fps,"frames per second")  
```

```python
# Get frame count
frame_count = vid_capture.get(7) #or cv2.CAP_PROP_FRAME_COUNT instead of 5
print("Frame count : ", frame_count)
```
