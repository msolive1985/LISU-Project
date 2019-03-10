"""joystickDaemon.py: Reads a joystick device using pygame and sends the information via UDP."""

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
UDP_IP = "127.0.0.1" # Localhost (for testing)
UDP_PORT = 7775 # This port match the ones using on other scripts

update_rate = 0.0595 # 100 hz loop cycle
# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
joyIndex = 0
packet_aux = ""

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

        packet = "bricktranslate " + str(round(roll,2)) + " " + str(round(pitch,2)) + " " + str(round(yaw,4))

        if(packet_aux == "" or packet_aux != packet):
            #sock.sendto(packet, (UDP_IP, UDP_PORT))  
            print packet
            packet_aux = packet
    
    # Make this loop work at update_rate
    while elapsed < update_rate:
        elapsed = time.time() - current
