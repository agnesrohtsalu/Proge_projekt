import dlib
import face_recognition
from PIL import Image
import cv2
image = face_recognition.load_image_file("naised.jpg")
face_locations = face_recognition.face_locations(image)
print(face_locations)
for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    cv2.imshow("nagu", face_image)
cv2.waitKey(0)