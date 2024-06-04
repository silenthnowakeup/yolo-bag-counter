import cv2
import os

cap = cv2.VideoCapture("../input/Задание.mp4")
frame_count = 0
dirname = "./images"
os.mkdir(dirname)
while True:
    ret, frame = cap.read()
    cv2.imshow("Frame", frame)
    frame_count += 1
    if frame_count % 100 == 0:
        cv2.imwrite(f"{dirname}/{frame_count}.jpg", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
