import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['arnold', 'bryan cranston', 'messi', 'steve jobs']

# let the recognizer read the training file
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# select image to recognize
img = cv.imread(r'test_imgs/messi (18).jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {round(confidence, 2)}%')
    
    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    
cv.imshow('Detected face', img)

cv.waitKey(0)
