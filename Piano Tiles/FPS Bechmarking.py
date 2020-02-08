import numpy as np
import time
import cv2
import mss
import mss.tools

# title of our window
title = "FPS benchmark"
# set start time to current time
start_time = time.time()
# displays the frame rate every 2 second
display_time = 2
# Set primarry FPS to 0
fps = 0
# Load mss library as sct
sct = mss.mss()
# Set monitor size to capture to MSS
monitor = {"top": 40, "left": 0, "width": 800, "height": 640}
# Set monitor size to capture
mon = (0, 40, 800, 640)
def screen_recordMSS():
    global fps, start_time
    while True:
        with mss.mss() as sct:
        # Get raw pixels from the screen, save it to a Numpy array
            img = sct.grab(monitor)
        ##        img = np.array(sct.grab(monitor))
            # to ger real color we do this:
##            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            #cv2.imshow(title, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
##            cv2.imshow(title, img)
            fps+=1
            TIME = time.time() - start_time
            if (TIME) >= display_time :
                print("FPS: ", fps / (TIME))
                fps = 0
                start_time = time.time()
            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord("q"):
                cv2.destroyAllWindows()
                break

screen_recordMSS()
##
##import numpy as np
##import cv2
##import mss
##import mss.tools
##from PIL import Image
##import time
##
##color = (0, 255, 0) # bounding box color.
##
### This defines the area on the screen.
##mon = {'top' : 10, 'left' : 10, 'width' : 1000, 'height' : 800}
##previous_time = 0
##with mss.mss() as sct :
##    while True:
##        img = sct.grab(mon)
##        frame = Image.frombytes('RGB', img.size, img.bgra, 'raw', 'BGRX')
##        frame = np.array(frame)
##        # image = image[ ::2, ::2, : ] # can be used to downgrade the input
##        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
##        cv2.imshow ('frame', frame)
##        if cv2.waitKey ( 1 ) & 0xff == ord( 'q' ) :
##            cv2.destroyAllWindows()
##            break
##        txt1 = 'fps: %.1f' % ( 1./( time.time() - previous_time ))
##        previous_time = time.time()
##        print (txt1)
