# -*- coding: utf-8 -*-
import cv2
import numpy as np

#カメラの取得 device_id=0
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #ハフ変換用にリサイズし、グレーカラーに変更
    frame = cv2.resize(frame, dsize=(640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (33, 33), 1)
    
    #ハフ変換による円形の抽出
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 60, param1=10, param2=85, minRadius=1, maxRadius=80)
    
    
    #変換結果がある場合にぴえんの描写を行う
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            #i[0]=x座標 i[1]=y座標 i[2]=半径
            x = i[0]; y = i[1]; r = i[2]
            #cv2.circleは円形 cv2.ellipseは楕円や楕円弧
            #輪郭
            cv2.circle(frame, (x, y), r, (0, 215, 255), -1)
            #眉毛右
            cv2.ellipse(frame, (x+int(r*2/3), y-int(r*2/3)), (int(r/3), int(r/4)), 0, 90, 165, (19, 69, 139), 3)
            #眉毛左
            cv2.ellipse(frame, (x-int(r*2/3), y-int(r*2/3)), (int(r/3), int(r/4)), 0, 15, 90, (19, 69, 139), 3)
            #涙右
            cv2.circle(frame, (x+int(r*2/5), y), int(r*3/10), (255, 255, 255), -1)
            #涙左
            cv2.circle(frame, (x-int(r*2/5), y), int(r*3/10), (255, 255, 255), -1)
            #黒目右
            cv2.circle(frame, (x+int(r*2/5), y-int(r/15)), int(r*3/10), (0, 0, 0), -1)
            #黒目左
            cv2.circle(frame, (x-int(r*2/5), y-int(r/15)), int(r*3/10), (0, 0, 0), -1)
            #白目大右
            cv2.ellipse(frame, ((x+int(r/3), y-int(r/6)), (int(r/3), int(r/4)), 135), (255, 255, 255), -1)
            #白目大左
            cv2.ellipse(frame, ((x-int(r/2), y-int(r/6)), (int(r/3), int(r/4)), 135), (255, 255, 255), -1)
            #白目小右
            cv2.ellipse(frame, ((x+int(r/2), y), (int(r/10), int(r/15)), 135), (255, 255, 255), -1)
            #白目小左
            cv2.ellipse(frame, ((x-int(r/3), y), (int(r/10), int(r/15)), 135), (255, 255, 255), -1)
            #口
            cv2.ellipse(frame, (x, y+r), (int(r/4), int(r/2)), 0, 245, 295, (19, 69, 139), 5)

    #ウィンドウにカメラの映像を表示 この時点でframeにはぴえんが描写されている
    cv2.imshow("frame", frame)

    #qキーを押したら終了する
    if cv2.waitKey(1)&0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
