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
UDP_PORT = 7755 # This port match the ones using on other scripts

update_rate = 0.095 # 100 hz loop cycle
# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
joyIndex = 1

try:
    pygame.init()
    pygame.joystick.init()

    joystick_count = pygame.joystick.get_count()

    #for jValue in range(joystick_count):
    #    auxJoy = pygame.joystick.Joystick(jValue)
    #    auxJoy.init()
    #    auxJoyName = joystick.get_name()
    #    if auxJoyName == "SL-6632 Dark Tornado Joystick":
    #        joyIndex = jValue
    
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
    #throttle = mapping(joystick.get_axis(3),1.0,-1.0,1000,2000)
    #mode     = joystick.get_button(24)

    # Be sure to always send the data as floats
    # The extra zeros on the message are there in order for the other scripts to do not complain about missing information
    #message = [roll, pitch, yaw, throttle, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    if(roll!=0.0 or pitch != 0.0 or yaw != 0.0):
        #packet = "translate " + str(roll) + " " + str(pitch) + " " + str(0.0) 
        #packet = "addrotation " + str(roll) + " " + str(pitch) + " " + str(yaw) + " " + str(10.0)
        packet = "addrotation " + str(roll) + " " + str(pitch) + " 0.0 " + str(10.0)
        sock.sendto(packet, (UDP_IP, UDP_PORT))  
        print packet
         #message = [packet]
         #buf = struct.pack('>' + 's' * len(message), *message)
         #sock.sendto(buf, (UDP_IP, UDP_PORT))  
         #print message

    # Make this loop work at update_rate
    while elapsed < update_rate:
        elapsed = time.time() - current
