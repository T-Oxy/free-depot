# -*- coding: utf-8 -*-
import cv2
import numpy as np

#カメラの取得 device_id=0
cap = cv2.VideoCapture(0)

#ban画像
anime_file = "ban.jpg"
anime_face = cv2.imread(anime_file)

def anime_face_func(img, rect):
    (x1, y1, x2, y2) = rect
    w = x2 - x1
    h = y2 - y1
    img_face = cv2.resize(anime_face, (w, h))
    
    img2 = img.copy()
    img2[y1:y2, x1:x2] = img_face
    return img2


while True:
    ret, frame = cap.read()
    #ハフ変換用にリサイズし、グレーカラーに変更
    frame = cv2.resize(frame, dsize=(640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (33, 33), 1)
    
    #ハフ変換による円形の抽出
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 60, param1=10, param2=85, minRadius=1, maxRadius=80)

    for (x, y, w, h) in circles:
        frame = anime_face_func(frame, (x, y, x+w, y+h))


    #ウィンドウにカメラの映像を表示
    cv2.imshow("frame", frame)

    #qキーを押したら終了する
    if cv2.waitKey(1)&0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
