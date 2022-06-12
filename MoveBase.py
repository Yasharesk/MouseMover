import pyautogui as pg
import time
from random import randint, choice

min_lag = 1
max_lag = 3

min_sleep = 5
max_sleep = 120

while True:
    """Get the size of the screen the cursor is on at the moment to set the range of movements"""
    max_x = pg.size().width
    max_y = pg.size().height
    """Wait for a random amount of time before each move"""
    time.sleep(randint(min_sleep, max_sleep))
    lag = randint(min_lag, max_lag)
    pg.moveTo(randint(0, max_x - 10), randint(0, max_y - 10), duration=lag)
    if choice([0,1,0]):
        pg.press('ctrlleft')
