# https://github.com/opencv/opencv

import sys

import cv2

# get user image name
imagePath = sys.argv[1]
cascPath = "frontalface_alt.xml"

# create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# read image
image = cv2.imread(imagePath)

# CV2 processes images by convert BRG in to gray
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the image
faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

print("Found {0} faces!".format(len(faces)))

# draw rectangle round the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)

# press any key to close image
cv2.waitKey()
