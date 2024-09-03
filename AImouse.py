import cv2 
import numpy as np
import mediapipe  as mp
from cvzone import HandTrackingModule as htm
import time
import pyautogui



wCam ,hCam = 640,480
cap = cv2.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)

hand_detector = mp.solutions.hands.Hands()
drawingUtils = mp.solutions.drawing_utils
screenheight,screenWidth = pyautogui.size()
indexY = 0
while True:
    success,frame = cap.read()
    frame = cv2.flip(frame,1)
    frameHeight,frameWidth,_ = frame.shape
    rgbFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgbFrame)
    
    hands = output.multi_hand_landmarks
    if hands:
         for hand in hands:
              drawingUtils.draw_landmarks(frame,hand)
              landmarks = hand.landmark
              for id, landmark in enumerate(landmarks):
                   x = int(landmark.x*frameWidth)
                   y = int(landmark.y*frameHeight)
                   #print(x,y)
                   if id ==8:
                        indexX =screenWidth/frameWidth*x
                        indexY =screenheight/frameHeight*y
                        cv2.circle(frame,(x,y),10,(200, 220, 21),cv2.FILLED)
                        pyautogui.moveTo(indexX,indexY)
                   if id ==4:
                        thumbX =screenWidth/frameWidth*x
                        thumbY =screenheight/frameHeight*y
                        cv2.circle(frame,(x,y),10,(200, 220, 21),cv2.FILLED)
                        print(abs(indexY-thumbY))
                        if abs(indexY-thumbY)<30:
                             #print("clicking")
                             pyautogui.click()
                             pyautogui.sleep(1)                             
                   

    cv2.imshow("Virtualmouse",frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
         cv2.destroyAllWindows()
         break
