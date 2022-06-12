from threading import Thread
import logging
import tkinter as tk
from tkinter import ttk
import time
from random import randint, choice
import pyautogui as pg
import configparser


logging.basicConfig(level=logging.ERROR, filename='main.log', format='%(asctime)s :: %(name)s :: %(levelname)s :: %(message)s')
logger = logging.getLogger(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

min_sleep = int(config['DEFAULT']['MIN_SLEEP'])
max_sleep = int(config['DEFAULT']['MAX_SLEEP'])
min_lag = int(config['DEFAULT']['MIN_LAG'])
max_lag = int(config['DEFAULT']['MAX_LAG'])
key_list = config['DEFAULT']['KEYBOARD_KEYS'].split(',')

def move():
    '''Start  a loop of moving the cursor around and press a key'''
    while True:
        if pause_flag == True:
            break
        max_x = pg.size().width
        max_y = pg.size().height
        """Wait for a random amount of time before each move"""
        logger.debug('Going to sleep')
        time.sleep(sleep_time := randint(min_sleep, max_sleep))
        logger.debug(f'{sleep_time=}')
        '''Set the amount of thime the cursor movement will take'''
        lag = randint(min_lag, max_lag)
        pg.moveTo(randint(0, max_x - 10), randint(0, max_y - 10), duration=lag)
        '''At some loops click one of the selected keyboard keys'''
        if choice([0,1]):
            pg.press(choice(key_list))


def start_thread():
    '''Change the state of the program to running'''
    global pause_flag 
    pause_flag =  False
    logger.debug(f'Satus changed to start and {pause_flag=}')
    start_button['state'] = 'disabled'
    pause_button['state'] = 'normal'
    t = Thread(target = move)
    t.start()


def stop_thread():
    '''Change the state of the program to paused'''
    global pause_flag
    pause_flag = True
    start_button['state'] = 'normal'
    pause_button['state'] = 'disabled'


'''Set up the GUI window'''
root = tk.Tk()
root.title('Move!')
root.iconbitmap(config['ASSETS']['ICON_FILE'])
window_width = int(config['DEFAULT']['WINDOW_WIDTH'])
window_height = int(config['DEFAULT']['WINDOW_HEIGHT'])
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f'{window_width}x{window_height}+{screen_width-window_width}+{screen_height-window_height-75}')
root.minsize(window_width, window_height)
'''Set up the buttons and link to the functions'''
start_button = ttk.Button(root, text='Start moving', command=start_thread, width=15)
start_button.pack(pady=25)
pause_button = ttk.Button(root, text="Take a break", command=stop_thread, width=15)
pause_button.pack()
pause_button['state'] = 'disabled'

root.mainloop()