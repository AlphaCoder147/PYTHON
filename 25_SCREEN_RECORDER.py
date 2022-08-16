import cv2
import pyautogui
import numpy

SCREEN_SIZE=(1920,1200)
FILE_NAME="sample.avi"
WINDOW_NAME="Screen Recorder"

cv2.namedWindow(WINDOW_NAME,cv2.WINDOW_NORMAL)
cv2.resizeWindow(WINDOW_NAME,400,400)

video_writer=cv2.VideoWriter(FILE_NAME,cv2.VideoWriter_fourcc(*"XVID"),20,SCREEN_SIZE)
while True:
    screen_shot=pyautogui.screenshot()
    frame=cv2.cvtColor(numpy.array(screen_shot),cv2.COLOR_BGR2RGB)
    video_writer.write(frame)
    cv2.imshow(WINDOW_NAME,frame)
    if cv2.waitKey(1)==27:
        break
video_writer.release()
cv2.destroyAllWindows()    