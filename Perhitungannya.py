import cv2
import time
import os
import tracking as htm

wCam, hCam = 1920, 1080

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]
def JariNaik(id):
    return lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]

def JariTurun(id):
    return lmList[tipIds[id]][2] > lmList[tipIds[id] - 2][2]

def JempolTurun():
    return lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]

def JempolNaik():
    return lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    img = cv2.flip(img,1) #Mengaur posisi kamera output
    #print(lmList)
    hehe = ("KALEM HIDUP MAH")

    if len(lmList) != 0:
        fingers = []

        if JariNaik(1):
            fingers.append(1)
            if JariNaik(2):
                fingers.append(1)
                if JempolNaik():
                    fingers.append(1)
                    if JariNaik(3) and JariTurun(4):
                        for jr in range (0,3):
                            fingers.append(1)
                    if JariNaik(3) and JariNaik(4):
                        for jr in range (0,2):
                            fingers.append(1)
                    if JariTurun(3) and JariNaik(4):
                        for jr in range (0,4):
                            fingers.append(1)  
                if JempolTurun():
                    if JariNaik(3) and JariNaik(4):
                        for jr in range (0,2):
                            fingers.append(1)

            if JariTurun(2):
                if JariNaik(3) and JariNaik(4) and JempolNaik():
                    for jr in range (0,7):
                        fingers.append(1)

                if JempolTurun() and JariNaik(3) and JariNaik(4):
                    for jr in range (0,2):
                            fingers.append(1)
        if JariTurun(1):
            if JariNaik(2) and JariNaik(3) and JariNaik(4) and JempolNaik():
               for jr in range (0,9):
                    fingers.append(1)
            if JariTurun(2) and JariTurun(3) and JariTurun(4) and JempolTurun():
                for jr in range (0,10):
                    fingers.append(1)

        else:
            fingers.append(0)
    
        print(fingers)
        totalFingers = fingers.count(1)
        #print(totalFingers)

        
            
        if JariNaik(1) and JariNaik(4) and JariTurun(2) and JariTurun(3) and JempolNaik():
            cv2.putText(img, str(hehe) , (10, 375), cv2.FONT_HERSHEY_PLAIN, 4, (251, 235, 217), 12) 
        elif JariTurun(1) and JariNaik(4) and JariNaik(2) and JariNaik(3) and JempolNaik():
            cv2.putText(img, str("Oke") , (10, 375), cv2.FONT_HERSHEY_PLAIN, 4, (251, 235, 217), 12) 
        else:
            cv2.rectangle(img, (0, 100), (100, 0), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(totalFingers), (10, 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 12)
   
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)