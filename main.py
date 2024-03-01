#import screennumberdetection as sd
import cv2
#import main as bd
#import elevatordoor as ed
import camera as wcam
#import time
wcam.cam()
'''bd.main()
bd.main_video()
#arm presses
wcam.cam()
time.sleep(5)
ed.iselevatoropen()
if (result=='closed'):
    wcam.cam()
elif result=='many people':
    wcam.cam()
else:
    print("enter")
    #enter


wcam.cam()
bd.main()
bd.main_video()
#arm presses


a=int(input('enter floor you want to go to:'))
print(sd.screennum(a))

img1 = cv2.imread('screen.jpeg')
print(bd.arrowdetection(img1))

IMAGE_PATH = 'buttons2.jpg'
img2=cv2.imread(IMAGE_PATH)
print(bd.buttondetection(IMAGE_PATH,img2))

img_frame_C = 'elev_close.jpg'
img_frame_O = 'elev_open.jpg'
print(ed.elevator_door(img_frame_C, img_frame_O))'''