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
  #logging.basicConfig(filename=("LISUJD.log"), level=logging.DEBUG, format='%(asctime)s, %(message)s')
  with open("LISU_6DOF.txt", "r") as ins:
        array = []
        for line in ins:
            array.append(line)      

  UDP_IP = "127.0.0.1"
  UDP_PORT = 7775
  update_rate = 0.5
  array_index = 0
  mapped_func = array[array_index]
  
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
    x = mapping(joystick.get_axis(0),-1.0,1.0,-1.0,1.0)
    y = mapping(joystick.get_axis(1),1.0,-1.0,-1.0,1.0)

    #roll     = mapping(joystick.get_axis(0),-1.0,1.0,-1.0,1.0)
    #pitch    = mapping(joystick.get_axis(1),1.0,-1.0,-1.0,1.0)
    #yaw      = mapping(joystick.get_axis(2),-1.0,1.0,-1.0,1.0)    

    #to calibrate
    if x < 0.07 and x > -0.07: x = 0.0
    if y < 0.07 and y > -0.07: y = 0.0
    
    #if(roll < 0.25 and roll > -0.25): roll = 0.0
    #if(pitch < 0.25 and pitch > -0.25): pitch = 0.0
    #if(yaw < 0.25 and pitch > -0.25): yaw = 0.0    

    for i in range(0, len(array)):#joystick.get_numbuttons()):
      if joystick.get_button(i) != 0:
        mapped_func = array[i]
    
    if(x != 0.0 or y != 0.0):
      print mapped_func.rstrip() + " " + str(round(x,2)) + " " + str(round(y,2)) + " 0.0"
      #print mapped_func.rstrip() + " " + str(round(roll,2)) + " " + str(round(pitch,2)) + " " + str(round(yaw,2))                
      #packet = "bricks_translate " + str(round(roll,2)) + " " + str(round(pitch,2)) + " " + str(round(yaw,2))
      #sock.sendto(packet, (UDP_IP, UDP_PORT))
      #logging.info("bricks_translate," + str(round(roll,2)) + "," + str(round(pitch,2)) + "," + str(round(yaw,2)))
            
    # Make this loop work at update_rate
    while elapsed < update_rate:
      elapsed = time.time() - current

if __name__ == "__main__":
  LISUJD(0)
  #LISUJD(joyIndex)
