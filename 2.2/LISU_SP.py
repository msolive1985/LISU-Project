"""LISU_SP.py: Reads a joystick device using pygame and sends the information via UDP."""

__author__ = "Mario Sandoval"
__copyright__ = "Copyright 2018"

__license__ = "The University of Manchester"
__version__ = "1"
__maintainer__ = "Mario Sandoval"
__email__ = "mario.sandovalolive@manchester.ac.uk"
__status__ = "Development"


import spacenavigator, socket, struct, time
import sys
import pygame
from modules.utils import *

# Main configuration
def LISUSP():
    UDP_IP = "127.0.0.1" # Localhost (for testing)
    UDP_PORT = 7755 # This port match the ones using on other scripts
    update_rate = 0.095 # 100 hz loop cycle

    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        success = spacenavigator.open()
        
    except Exception,error:
        print "No spacenavigator connected on the computer, "+ str(error)

    if success:
        while True:
            current = time.time()
            elapsed = 0               

            state = spacenavigator.read()            
            roll     = state.x
            pitch    = state.y
            yaw      = state.z
                        
            if(roll!=0.0 or pitch != 0.0 or yaw != 0.0):
                #packet = "bricks_translate " + str(round(roll,2)) + " " + str(round(pitch,2)) + " " + str(round(yaw,2)) + " 2 "
                packet = "addrotation " + str(round(roll,2)) + " " + str(round(pitch,2)) + " " + str(round(yaw,2)) + " " + str(10.0)
                sock.sendto(packet, (UDP_IP, UDP_PORT))
                print packet
                time.sleep(0.5)
			
            # Make this loop work at update_rate
            while elapsed < update_rate:
                elapsed = time.time() - current

if __name__ == "__main__":
    LISUSP()