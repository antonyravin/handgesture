import cv2
import serial
import time
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)  # Allow 1 hand

arduino = serial.Serial('COM4', 9600)
time.sleep(2)  # Give Arduino time to reset

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Mirror the webcam image

    #hands, img = detector.findHands(img, flipType=False)

    hands, img = detector.findHands(img)
    if hands:
        fingers = detector.fingersUp(hands[0])
        count = fingers.count(1)
        arduino.write(str(count).encode())  # Send count
        print("Fingers:", count)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
