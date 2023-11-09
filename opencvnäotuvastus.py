import cv2

face_cascade = cv2.CascadeClassifier('C:/Users/Dell/Desktop/proge_projekt/haarcascade_frontalface_default.xml')
img_path = 'C:/Users/Dell/Desktop/proge_projekt/teet.jpg'
img = cv2.imread(img_path)

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

    cv2.imshow('img', img)
    cv2.waitKey()
else:
    print(f"Error: Unable to load image from path {img_path}")
