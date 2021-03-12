import cv2
import time
import imutils
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second


cam = cv2.VideoCapture(0)
time.sleep(1)
frame_width = int(cam.get(3))
frame_height = int(cam.get(4))

size = (frame_width, frame_height)
# size = (width, height)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter("your_video2.avi", fourcc , 20.0, size)


firstFrame=None
area = 500

while True:
    _,img = cam.read()
    text = "Normal"
    # img = imutils.resize(img, width=400)
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussianImg = cv2.GaussianBlur(grayImg, (5, 5), 0)
    if firstFrame is None:
            firstFrame = gaussianImg
            continue
    imgDiff = cv2.absdiff(firstFrame, gaussianImg)
    # cv2.imshow("hi",imgDiff)
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
    # cv2.imshow("hi", threshImg)
    # threshImg = cv2.erode(threshImg, None, iterations=2)
    threshImg = cv2.dilate(threshImg, None, iterations=4)
    cv2.imshow("ji",threshImg)
    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    count=0
    for c in cnts:
            if cv2.contourArea(c) < 1000:
                    continue
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Moving Object detected"
            count+=1
    if count>0:
        winsound.Beep(frequency, duration)
    # print(count==len(cnts))
    print(text,count)
    cv2.putText(img, text+" " +str(count), (10, 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    out.write(img)
    cv2.imshow("cameraFeed",img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
out.release()#saves video
cv2.destroyAllWindows()
