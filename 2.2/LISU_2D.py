"""LISU_2D.py: Reads the info from the mouse."""

__author__ = "Mario Sandoval"
__copyright__ = "Copyright 2018"
__license__ = "The University of Manchester"
__version__ = "2.2.1"
__maintainer__ = "Mario Sandoval"
__email__ = "mario.sandovalolive@manchester.ac.uk"
__status__ = "Development"

from pynput.keyboard import Listener  as KeyboardListener
from pynput.mouse    import Listener  as MouseListener
from pynput.keyboard import Key
import logging

logging.basicConfig(filename=("LISU_P0.log"), level=logging.DEBUG, format='%(asctime)s, %(message)s')

def end_rec(key):
    logging.info(str(key))

def on_press(key):
    return False

def on_move(x, y):
    logging.info("Mouse moved, {0}, {1}".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked, {0}, {1}'.format(x, y))

def LISU2D():
    with MouseListener(on_click=on_click) as listener:
        with KeyboardListener(on_press=on_press) as listener:
            listener.join()

if __name__ == "__main__":
    try:
        LISU2D()
    except KeyboardInterrupt:
        sys.exit()   
