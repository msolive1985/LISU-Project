"""LISU_2D.py: Reads the info from the mouse."""

__author__ = "Mario Sandoval"
__copyright__ = "Copyright 2018"
__license__ = "The University of Manchester"
__version__ = "2.2"
__maintainer__ = "Mario Sandoval"
__email__ = "mario.sandovalolive@manchester.ac.uk"
__status__ = "Development"

from pynput.mouse import Listener
import logging

logging.basicConfig(filename=("LISU2D.log"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

def LISU2D():
    with Listener(on_move=on_move, on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    try:
        LISU2D()
    except KeyboardInterrupt:
        sys.exit()   
