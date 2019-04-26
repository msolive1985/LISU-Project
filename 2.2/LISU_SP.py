"""LISU_SP.py: Reads a joystick device using pygame and sends the information via UDP."""
__author__ = "Mario Sandoval"
__copyright__ = "Copyright 2018"
__license__ = "The University of Manchester"
__version__ = "2.2"
__maintainer__ = "Mario Sandoval"
__email__ = "mario.sandovalolive@manchester.ac.uk"
__status__ = "Development"

import spacenavigator, socket, struct, time
import pygame, random, sys, logging
import datetime
from modules.utils import *

def LISUSP():
    currentDT = datetime.datetime.now()
    record = currentDT.year + currentDT.month + currentDT.day
    logging.basicConfig(filename=("LISUSP.txt"), level=logging.DEBUG, format='%(asctime)s, %(message)s')

    UDP_IP = "127.0.0.1" 
    UDP_PORT = 7755 
    update_rate = 0.095    
    
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
                packet = "addrotation " + str(round(roll,2)) + " " + str(round(pitch,2)) + " " + str(round(yaw,2)) + " " + str(10.0)
                sock.sendto(packet, (UDP_IP, UDP_PORT))
                logging.info("addrotation, " + str(round(roll,2)) + ", " + str(round(pitch,2)) + ", " + str(round(yaw,2)) + ", " + str(10.0))
                time.sleep(0.5)
			
            while elapsed < update_rate:
                elapsed = time.time() - current		    

#if __name__ == "__main__":
#    LISUSP()
