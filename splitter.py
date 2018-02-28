import cv2
print(cv2.__version__)
filename = "Lake_Street_Dive_-_Spectacular_Failure-LXDl3fBmFZ8.mp4"
vidcap = cv2.VideoCapture(filename)
success,image = vidcap.read()
count = 0
success = True
while success:
    cv2.imwrite("frame{0}.png".format(count),image)
    success, image = vidcap.read()
    print("new frame {0}".format(count))
    count = count + 1
    if count > 10:
        break
