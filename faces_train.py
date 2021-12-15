import os
import cv2 as cv
import numpy as np

people = []
DIR = r'train_imgs'
for i in os.listdir(DIR):
    people.append(i)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

def create_training():
    # loop over every person in list and get persons path and label
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)
        
        # loop to get to specific images and convert to gray to use haar-cascade and get the faces
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
            
            # loop over coordinates in images to get the region of interest and append to features and label them
            for (x,y,w,h) in faces_rect: 
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_training()

# convert to numpy arrays for use in face recognizer
features = np.array(features, dtype='object')
labels = np.array(labels)

# initialize recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features and the labels lists
face_recognizer.train(features, labels)
print('Training complete ---------------------')

face_recognizer.save('face_trained.yml')
