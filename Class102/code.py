import cv2
import random
import time

startTime = time.time()

def snapShot():
    number = random.randint(1,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret, frame = videoCaptureObject.read()
        name = "Pic" + str(number) + ".png"
        cv2.imwrite(name, frame)
        startTime = time.time
        result = False
    
    return name
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def main():
    while(True):
        if((time.time()-startTime)>=60):
            ImgName = snapShot()

main()