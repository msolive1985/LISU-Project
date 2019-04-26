"""LISU_WD.py: Reads the Wing device using pygame and sends the information via UDP."""

__author__ = "Mario Sandoval"
__copyright__ = "Copyright 2018"
__license__ = "The University of Manchester"
__version__ = "2.2"
__maintainer__ = "Mario Sandoval"
__email__ = "mario.sandovalolive@manchester.ac.uk"
__status__ = "Development"

import socket, struct, time
import pygame, random, sys, logging
from modules.utils import *

def autocalibrateValues(value, sigma):
    rValue = value
    varAux = value + sigma
    if varAux > 0 and varAux <= sigma:
        rValue = 0.0
    if varAux < 0 and varAux >= -(sigma):
        rValue = 0.0
    return rValue

def LISUWD(joyIndex):
    logging.basicConfig(filename=("LISUWD.log"), level=logging.DEBUG, format='%(asctime)s, %(message)s')
    UDP_IP = "127.0.0.1"
    UDP_PORT = 7755
    update_rate = 0.75        
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #joyIndex = 2
    sigmaWing = 0.5    

    try:
        pygame.init()
        pygame.joystick.init()
        wingControl = pygame.joystick.Joystick(joyIndex)
        wingControl.init()
    except Exception,error:
        print "No joystick connected on the computer, "+str(error)

    while True:
        current = time.time()
        elapsed = 0   

        # Joystick reading
        pygame.event.pump()
        roll     = mapping(wingControl.get_axis(0),-1.0,1.0,-1.0,1.0)
        pitch    = mapping(wingControl.get_axis(1),1.0,-1.0,-1.0,1.0)
        yaw      = mapping(wingControl.get_axis(3),1.0,-1.0,-1.0,1.0)		
        #throttle = mapping(joystick.get_axis(3),1.0,-1.0,-1.0,1.0)
        #mode     = joystick.get_button(24)

        # Autocalibrate values
        roll = autocalibrateValues(roll, sigmaWing)
        pitch = autocalibrateValues(pitch, sigmaWing)
        yaw = autocalibrateValues(yaw, sigmaWing)

        #For the queue
        if(roll < 0.25 and roll > -0.25): roll = 0.0
        if(pitch < 0.25 and pitch > -0.25): pitch = 0.0
        if(yaw < 0.25 and pitch > -0.25): yaw = 0.0
                
        if(roll!=0.0 or pitch != 0.0 or yaw != 0.0):
            packet = "addrotation " + str(round(roll,2)) + " " + str(round(pitch,2)) + " " + str(round(yaw,2)) + " " + str(10.0)
            sock.sendto(packet, (UDP_IP, UDP_PORT))
	    logging.info("addrotation, " + str(round(roll,2)) + ", " + str(round(pitch,2)) + ", " + str(round(yaw,2)) + ", " + str(10.0))
			
        # Make this loop work at update_rate
        while elapsed < update_rate:
            elapsed = time.time() - current

#if __name__ == "__main__":
#    LISUWD()
