"""spaceNavDaemon.py: Reads a joystick device using pygame and sends the information via UDP."""

__author__ = "Mario Sandoval"
__copyright__ = "Copyright 2018"
__license__ = "The University of Manchester"
__version__ = "1"
__maintainer__ = "Mario Sandoval"
__email__ = "mario.sandovalolive@manchester.ac.uk"
__status__ = "Development"

import socket, struct, time
import sys
import pygame
from modules.utils import *

# Main configuration
def autocalibrateValues(value, sigma):
    try:
        varAux = sigma - abs(value)        
        if varAux > 0.0 and varAux <= sigma:
            varAux = 0.0
        else:
            varAux = value        
        return varAux
    except Exception,error:
        print "ERROR: "+str(error)
        varAux = 0.0
        return varAux

def spaceNav_Daemon():
    UDP_IP = "127.0.0.1" # Localhost (for testing)
    UDP_PORT = 7755 # This port match the ones using on other scripts

    update_rate = 0.095 # 100 hz loop cycle
    joyIndex = 1
    sigmaWing = 0.2 # With seven: 0.115637 # Originally: 0.008858 

    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    

    try:
        pygame.init()
        pygame.joystick.init()
        joystick = pygame.joystick.Joystick(joyIndex)
        joystick.init()
    except Exception,error:
        print "No joystick connected on the computer, "+str(error)

    while True:
        current = time.time()
        elapsed = 0
   
        # Joystick reading
        pygame.event.pump()
        roll     = mapping(joystick.get_axis(0),-1.0,1.0,-1.0,1.0)
        pitch    = mapping(joystick.get_axis(1),1.0,-1.0,-1.0,1.0)
        yaw      = mapping(joystick.get_axis(2),1.0,-1.0,-1.0,1.0)
        #throttle = mapping(joystick.get_axis(3),1.0,-1.0,-1.0,1.0)
        #mode     = joystick.get_button(24)

        # Autocalibrate values
        roll = autocalibrateValues(roll, sigmaWing)
        pitch = autocalibrateValues(pitch, sigmaWing)
        yaw = 0.0 #autocalibrateValues(yaw, sigmaWing)

        if(roll!=0.0 or pitch != 0.0 or yaw != 0.0):
            packet = "addrotation " + str(roll) + " " + str(pitch) + " " + str(yaw) + " " + str(10.0)
            sock.sendto(packet, (UDP_IP, UDP_PORT))  
            print packet

        # Make this loop work at update_rate
        while elapsed < update_rate:
            elapsed = time.time() - current

if __name__ == "__main__":
    spaceNav_Daemon()
