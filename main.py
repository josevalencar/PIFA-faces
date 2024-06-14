import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

cap = cv2.VideoCapture('la_cabra.mp4')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_cascade2 = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
video = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, image = cap.read()

    if not ret:
      break

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(70, 70))
    faces_2 = face_cascade2.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(70, 70))

    for (x, y, w, h) in faces:
        if (x, y, w, h) in faces_2:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    video.write(image)

    cv2.waitKey(1) & 0xff

video.release()
cv2.destroyAllWindows()
cap.release()