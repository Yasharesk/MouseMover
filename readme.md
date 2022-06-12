# MouseMover

Simply as the name suggests, this script moves the mouse around in random intervals to random points of the screen to keep your screen active.  
This has been just a practice for creating a separate thread for handling the movement loop alongside the main loop of the GUI on the Move.py


### Movebase.py
This is simple script to be ran with Python. It only requires the __pyautogui__ package installed.

### Move.py
This is the GUI version wich uses tkinter to create as simple window with two buttons that start and pause the movement loop. Use pyinstaller to create executable vesrion. 
```sh
pyinstaller Move.py --noconsole
```

Some minor customizaitons on window size, time interval limits between moves and so on can be acheived by editing the config.ini file. 

