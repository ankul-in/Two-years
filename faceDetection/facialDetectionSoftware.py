#https://youtu.be/JZZr0PjZsIk

import cv2

# This automatically finds the correct path
face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#face_cap = cv2.CascadeClassifier(r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python313\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)
print("press 'q' to quit")
while True:
    ret , videoData = video_cap.read()
    col = cv2.cvtColor(videoData,cv2.COLOR_BGR2GRAY)
    faces=face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE

    )
    for(x,y,w,h) in faces:
        cv2.rectangle(videoData,(x,y),(x+w,y+h),(135, 206, 235),2)
    cv2.imshow("videoLive",videoData)
    if cv2.waitKey(10) == ord("q"):
        break
video_cap.release()



# only for video
#video_cap = cv2.VideoCapture(0)
# while True:
#     ret , videoData = video_cap.read()
#     cv2.imshow("videoLive",videoData)
#     if cv2.waitKey(10) == ord("a"):
#         break
# video_cap.release()
