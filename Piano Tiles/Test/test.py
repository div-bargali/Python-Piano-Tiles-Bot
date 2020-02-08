import numpy as np
import cv2
import mss
import mss.tools
import pyautogui as pt
from PIL import Image
import time
import matplotlib.pyplot as plt

##gameCoords = (669, 542, 1248, 543) Second best
##gameCoords = (669, 735, 1248, 736)
gameCoords1 = (660,50 , 1248, 780)
gameCoords2 = (706+150, 58, 707+150, 780)
gameCoords3 = (706+300, 58, 707+300, 780)
gameCoords4 = (706+450, 58, 707+450, 780)
# top, left, right, bottom
cords_x = [57, 223, 384, 535]
w = gameCoords1[2] - gameCoords1[0]
x = 0
gamecoords = (660 ,50 , 661, 780)

def main():
    pt.FAILSAFE = True
    gameCoords = (660+x ,50 , 661+x, 780)
    
    while True:
        with mss.mss() as sct:
            pqueue = []
            start_time = time.time()
            for cord in cords_x:
                frame = sct.grab(gameCoords)
                for y in range(715, 0, -70):
                    if frame.pixel(0,y)[0] < 100:
                        pqueue.append(y)
            actual_y = max(pqueue)
            index = pqueue.index(actual_y)

            pt.click(gamecoords[0]+cords_x[index], actual_y+gamecoords[1], interval=0)
                    
            print(time.time()-start_time)
            pqueue.clear()   


def test():
    pt.FAILSAFE = True
    with mss.mss() as sct:
        while True:
            start_time = time.time()
            sct_img = sct.grab(gameCoords)
            for cord in cords_x:       
                
                for y in range(708,0):
                    if sct_img.pixel(cord,y)[0] < 100:
                        if y+gameCoords[1] > 536:
                            pt.click(gameCoords[0]+cord, y+gameCoords[1], interval=0)
            print(time.time()-start_time)

def test2():
    pt.FAILSAFE = True
    while True:
        with mss.mss() as sct:
            start_time = time.time()
            sct_img = sct.grab(gameCoords1)
            for cord in cords_x:
                for y in range(0, 780-58,100):
                    if sct_img.pixel(cord, y)[0] < 100:
                        pt.click(gameCoords1[0]+cord , y+gameCoords[1], interval=0)
        print(time.time()-start_time)
        
time.sleep(3)
main()


