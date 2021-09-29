import matplotlib.pyplot as plt
import cv2
 
cascade_file= "haarcascade_frontalface_alt.xml"
clas = cv2.CascadeClassifier(cascade_file)
 
img = cv2.imread("woman.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_list = clas.detectMultiScale(img_gray, minSize=(150,150))
 
print(face_list)
x=face_list[0][0]
y=face_list[0][1]
w=face_list[0][2]
h=face_list[0][3]
 
print("face(x,y,w,h):", x, y, w, h)
red=(0,0,255)
cv2.rectangle(img, (x,y), (x+w, y+h), red, thickness=20)
 
face= img[y:y+h, x:x+w]
reduc = cv2.resize(face, (8,8))
mosaic = cv2.resize(reduc,(w,h))
img[y:y+h, x:x+w]=mosaic
 
cv2.imwrite("face-mosaic.jpg", img)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
