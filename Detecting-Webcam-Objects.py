import cv2, time

first_frame = None


video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21),0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)   #To compare two gray scale images

    """If the values that is the difference between the first frame and the current frame is 
    more than 30 then we will classify that as white, it means the object is in motion else if
    the difference is less than 30 we classify it as black. Actual frame is present at the 
    second position when we use any threshold method that is why extracting index position [1]"""
    
    thresh_frame = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1] 
    thresh_frame = cv2.dilate(thresh_frame,None,iterations=2) #To smoothen the threshold frame

    cv2.imshow("GrayFrame", gray)
    cv2.imshow("DeltaFrame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    key = cv2.waitKey(1)
    print(gray)
    print(delta_frame)

    if key == ord('q'):
        break

video.release()    
cv2.destroyAllWindows()