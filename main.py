import cv2

# Loading the required haar-cascade xml classifier file
haar_cascade = cv2.CascadeClassifier('resource/haarcascade_russian_plate_number.xml')

cap=cv2.VideoCapture(0)
count=0
while True:
    sucess,img=cap.read()

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



    # Applying the face detection method on the grayscale image
    faces_rect = haar_cascade.detectMultiScale(gray_img, 1.1, 9)

    # Iterating through rectangles of detected faces
    for (x, y, w, h) in faces_rect:
        area=w*h
        if area>500:
          cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
          crop_img=img[y:y+h,x:x+w]
          cv2.imshow("Croped",crop_img)


    cv2.imshow("Out",img)

    if cv2.waitKey(1)&0xFF==ord('S'):

        cv2.imwrite("resource/saved/Noplate_"+str(count)+".jpg",crop_img)
        count+=1
