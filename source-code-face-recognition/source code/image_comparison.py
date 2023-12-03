import cv2
import face_recognition

# Load the first image
img = cv2.imread("source-code-face-recognition/source code/images/Elon Musk.jpg")
if img is None:
    print("Error: Image not loaded.")
    exit()

rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

# Load the second image
img2 = cv2.imread("source-code-face-recognition/source code/images/Jeff Bezoz.jpg")
if img2 is None:
    print("Error: Image 2 not loaded.")
    exit()

rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

result = face_recognition.compare_faces([img_encoding], img_encoding2)
print("Result: ", result)

cv2.imshow("Img", img)
cv2.imshow("Img 2", img2)
cv2.waitKey(0)