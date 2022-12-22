#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

Nfing = []
cap = cv2.VideoCapture(0)
listy = [0]*21
total = 0
#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #collect position y-axis in listy at id key
                for i in range(21):
                    if id == i:
                        listy[i] = cy
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    #check data in list
    if len(listy) != 0:
        #comparison between position for count stand finger 
        if listy[4]<listy[9]: #thumb (if true will count 1)
            t = 1
        else:
            t = 0
        if listy[8]<listy[7]:#index finger
            r = 1
        else:
            r = 0
        if listy[12]<listy[11]:#middle finger
            c = 1
        else:
            c = 0
        if listy[16]<listy[15]:#ring finger
            k = 1
        else:
            k = 0
        if listy[20]<listy[19]:#pinky 
            l = 1    
        else:
            l = 0   
        #summary stand finger
        total = t+r+c+k+l 
    #show opencv and summary  
    cv2.putText(img, str(int(total)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()