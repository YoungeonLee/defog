# Reference
# https://www.geeksforgeeks.org/extract-images-from-video-in-python/

# The first image and its laplacian variance is recorded then image subsequent
# images with value greater than the threshold (10 in the below example) gets 
# recorded.

# Importing all necessary libraries 
import cv2 
import os 

# Read the video from specified path 
cam = cv2.VideoCapture("./test-video.mp4") 

try: 
    # creating a folder named data 
    if not os.path.exists('data'): 
        os.makedirs('data') 

# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 

# frame 
currentframe = 0

last_variance = float('inf')
every_x_variance = 10

while(True): 
    # reading from frame 
    ret,frame = cam.read()

    if ret: # if video is still left continue creating images 
        variance = cv2.Laplacian(frame, cv2.CV_32F).var()
        
        # record next variance:
        if variance < last_variance - every_x_variance:
            name = './data/frame' + str(currentframe) + 'var' + str(variance) + '.jpg'
            print ('Creating...' + name)
            
            # writing the extracted images
            cv2.imwrite(name, frame) 
            last_variance = variance    
            
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
    else: 
        break

# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 
