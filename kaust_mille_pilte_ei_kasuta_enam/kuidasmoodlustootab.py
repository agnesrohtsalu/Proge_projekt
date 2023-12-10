# import face_recognition

# # Load the jpg files into numpy arrays
# biden_image = face_recognition.load_image_file("/home/agnesrohtsalu/Desktop/Proge_projekt/isikud/biden.jpg")
# obama_image = face_recognition.load_image_file("/home/agnesrohtsalu/Desktop/Proge_projekt/isikud/obama.jpg")
# unknown_image = face_recognition.load_image_file("/home/agnesrohtsalu/Desktop/Proge_projekt/isikud/obama2.jpg")

# # Get the face encodings for each face in each image file
# # Since there could be more than one face in each image, it returns a list of encodings.
# # But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
# try:
#     biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
#     obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
#     unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
# except IndexError:
#     print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
#     quit()

# isikud = [
#     biden_face_encoding,
#     obama_face_encoding
# ]

# # results is an array of True/False telling if the unknown face matched anyone in the isikud array
# results = face_recognition.compare_faces(isikud, unknown_face_encoding)

# print("Is the unknown face a picture of Biden? {}".format(results[0]))
# print("Is the unknown face a picture of Obama? {}".format(results[1]))
# print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))


import face_recognition
import os

# Path to the folder containing images of known people
isikud_folder = "/home/agnesrohtsalu/Desktop/Proge_projekt/isikud"

# Load the images and create an array of face encodings
isikud = []

for filename in os.listdir(isikud_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(isikud_folder, filename)
        known_image = face_recognition.load_image_file(image_path)
        try:
            face_encoding = face_recognition.face_encodings(known_image)[0]
            isikud.append(face_encoding)
        except IndexError:
            print(f"Skipping {filename}: No face found.")

# Load the unknown image
unknown_image_path = "/home/agnesrohtsalu/Desktop/Proge_projekt/isikud/obama2.jpg"
unknown_image = face_recognition.load_image_file(unknown_image_path)
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare the unknown face encoding with known face encodings
results = face_recognition.compare_faces(isikud, unknown_face_encoding)

# Print the results
for i, result in enumerate(results):
    print(f"Is the unknown face a picture of person {i+1}? {result}")
