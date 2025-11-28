import cv2
import mediapipe as mp
import time
5

class HandDetector():
    def __init__(self, mode=False, max_hands=1, complexity=1, detectionCon=0.5, trackingCon=0.5):
        self.mode = mode
        self.max_hands = max_hands
        self.complexity = complexity
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.max_hands, self.complexity, self.detectionCon, self.trackingCon)
        self.mpDraw = mp.solutions.drawing_utils

    def detecthands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # img132 = cv2.imread
        self.result = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)
        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw:
                    # for id, lm in enumerate(handLms.landmark):
                    #     h, w, c = img.shape
                    #     cx, cy = int(lm.x * w), int(lm.y * h)
                    #     # print(id,w,h)
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def handcordinate(self, img,lm_id=0, handnNo=0, draw=True):
        lmList = []
        if self.result.multi_hand_landmarks:
            myhand = self.result.multi_hand_landmarks[handnNo]
            for id, lm in enumerate(myhand.landmark):
                h, w , c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                # print(lmList[4])
                if draw == True:
                    cv2.putText(img, str(id), (cx, cy + 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
                    if id == 0:
                        cv2.circle(img, (cx, cy), 10, (0, 0, 0), cv2.FILLED)
                    if id > 0 and id <= 4:
                        cv2.circle(img, (cx, cy), 10, (245, 136, 20), cv2.FILLED)
                    if id > 4 and id <= 8:
                        cv2.circle(img, (cx, cy), 10, (237, 7, 7), cv2.FILLED)
                    if id > 8 and id <= 12:
                        cv2.circle(img, (cx, cy), 10, (57, 245, 20), cv2.FILLED)
                    if id > 12 and id <= 16:
                        cv2.circle(img, (cx, cy), 10, (245, 20, 144), cv2.FILLED)
                    if id > 16 and id <= 21:
                        cv2.circle(img, (cx, cy), 10, (230, 23, 223), cv2.FILLED)
        if len(lmList) != 0 and draw == True:
            cv2.putText(img, str(lmList[lm_id]), (400, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        return lmList


def main():
    cTime = 0
    pTime = 0
    lm_id = int(input("enter landmark id(0 to 20):"))
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    while True:
        success, img = cap.read()
        img = detector.detecthands(img)
        if lm_id<21:
            detector.handcordinate(img, lm_id)
        else:
            cv2.putText(img, str("landmark_id not in range"), (310, 30), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (5, 40), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        cv2.imshow("image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
