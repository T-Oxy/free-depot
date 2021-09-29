import cv2
import numpy as np

#Webカメラから入力
cap = cv2.VideoCapture(0)

#動画書き出し用のオブジェクト
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

fps = 15.0
size = (640, 360)
# writer = cv2.VideoWriter('out1.m4v', fmt, fps, size)
writer = cv2.VideoWriter('face_to_ban.mp4', fmt, fps, size)



#face5
face_cascade_file5 = "haarcascade_frontalface_default.xml"
face_cascade_5 = cv2.CascadeClassifier(face_cascade_file5)

#画像
anime_file = "img/ban6.jpg"
anime_face = cv2.imread(anime_file)
print(anime_face.shape)
anime2_file = "img/ban5.jpg"
anime2_face = cv2.imread(anime2_file)
anime3_file = "img/ban7.png"
anime3_face = cv2.imread(anime3_file)
anime4_file = "img/ban8.jpg"
anime4_face = cv2.imread(anime4_file)
anime5_file = "img/ban9.png"
anime5_face = cv2.imread(anime5_file)

def anime_face_func(img, rect):
    (x1, y1, x2, y2) = rect
    w = x2 - x1
    h = y2 - y1
    if(w < 135):
        img_face = cv2.resize(anime_face, (w, h))
    elif(135 <= w < 145):
        img_face = cv2.resize(anime2_face, (w, h))
    elif(145 <= w < 155):
        img_face = cv2.resize(anime3_face, (w, h))
    elif(155 <= w < 165):
        img_face = cv2.resize(anime4_face, (w, h))
    else:
        img_face = cv2.resize(anime5_face, (w, h))

    img2 = img.copy()
    img2[y1:y2, x1:x2] = img_face
    return img2


while True:
    #画像を取得
    _, img = cap.read()
    img = cv2.resize(img, size)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade_5.detectMultiScale(gray, 1.1, 2)
    
    
    for (x, y, w, h) in faces:
        img = anime_face_func(img, (x, y, x+w, y+h))



    writer.write(img)

    cv2.imshow('img', img)

    #ESCかEnterキーが押されたら終了
    k = cv2.waitKey(1)
    if k == 13:
        break

writer.release()
cap.release()
cv2.destroyAllWindows()
