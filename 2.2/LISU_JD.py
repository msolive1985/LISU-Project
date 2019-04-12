"""LISU_JD.py: Reads a joystick device using pygame and sends the information via UDP."""

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

def LISUJD(joyIndex):
        logging.basicConfig(filename=("LISUJD.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
        UDP_IP = "127.0.0.1"
	UDP_PORT = 7775
	update_rate = 0.0595	
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	#joyIndex = 0
	try:
                pygame.init()
		pygame.joystick.init()
		joystick_count = pygame.joystick.get_count()    
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
		yaw      = mapping(joystick.get_axis(2),-1.0,1.0,-1.0,1.0)    
		#For the queue
		if(roll < 0.25 and roll > -0.25): roll = 0.0
		if(pitch < 0.25 and pitch > -0.25): pitch = 0.0
		if(yaw < 0.25 and pitch > -0.25): yaw = 0.0    
    
		if(roll!=0.0 or pitch != 0.0 or yaw != 0.0):
			packet = "bricks_translate " + str(round(roll,2)) + " " + str(round(pitch,2)) + " " + str(round(yaw,2)) + " 1 "
                        sock.sendto(packet, (UDP_IP, UDP_PORT))
                        logging.info(packet)
            
		# Make this loop work at update_rate
		while elapsed < update_rate:
			elapsed = time.time() - current

#if __name__ == "__main__":
#    LISUJD(joyIndex)
