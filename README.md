# Python-Piano-Tiles-Bot
This bot uses image processing with Open CV to play the game of Piano Tiles.

Prerequisites:

Python 3.6 or above
Numpy
Mss
Pyautogui
Open CV

Working:

The script uses mss to grab images from the gamescreen. To benchmark the FPS of capture run "FPS Bechmark.py". (I got around 20 fps which was decent for upto the score of 1k).
The bounding box is defined as 1 pixel wide column and the script takes 4 images of pre-defined regions (the four centres in this case). Then the script looks for the darkest pixel which is at the lowest region of the bounding box (this compensates for clicking on a tile before clicking on the lowest tile).
Pyautogui is used to automate the mouse click at the certain pixel. 

Improvements:

At faster levels when 20 FPS of screen capture is not enough, the script can be improved by calculating the speed of the tile by capturing it by 2 relative positions and then predicting where the tile will be after a certain time.

