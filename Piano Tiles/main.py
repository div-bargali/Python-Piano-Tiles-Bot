import numpy as np
import cv2
import mss
import mss.tools
import pyautogui as pt
from PIL import Image
import time

##gameCoords = (669, 542, 1248, 543) Second best
##gameCoords = (669, 735, 1248, 736)
gameCoords = (669, 536, 1248, 537)
cords_x = [57, 223, 384, 535]
##smallerGameCoords = (657, 800, 1262, 802)
##score = 0
##previousLane = -1

def clickonBlock(screen):
    global gameCoords
     

def main():
    score = 0
    while True:
        pt.FAILSAFE = True
        with mss.mss() as sct:
            sct_img = sct.grab(gameCoords)

            start_time = time.time()
            for cord in cords_x:
                if sct_img.pixel(cord,0)[0] < 100:
                    pt.click(gameCoords[0]+cord, gameCoords[1] , interval=0)
                
            
        ##        for cords in cords_x:
        ##            if screen[cords][0] < 100:
        ##                pt.click(gameCoords[0]+cord , gameCoords[1])
        ##                break
            print(time.time()-start_time)
           
##        if cv2.waitKey(25) & 0xFF == ord('q'):
##            cv2.destroyAllWindows()
##            break


def test():
    pt.FAILSAFE = True
    time.sleep(3)
    with mss.mss() as sct:
        sct_img = sct.grab(gameCoords)

        start_time = time.time()
        for cord in cords_x:
            if sct_img.pixel(cord,0)[0] < 100:
                pt.click(gameCoords[0]+cord, gameCoords[1])
        
    ##        for cords in cords_x:
    ##            if screen[cords][0] < 100:
    ##                pt.click(gameCoords[0]+cord , gameCoords[1])
    ##                break
        print(time.time()-start_time)
time.sleep(3)
main()

