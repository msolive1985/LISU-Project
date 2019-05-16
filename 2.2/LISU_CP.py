"""LISU_CP.py: """

__author__ = "Mario Sandoval"
__copyright__ = "Copyright 2018"
__license__ = "The University of Manchester"
__version__ = "2.2"
__maintainer__ = "Mario Sandoval"
__email__ = "mario.sandovalolive@manchester.ac.uk"
__status__ = "Development"

import socket, struct, time
import pygame, random, sys
from modules.utils import *

from threading import Thread
from LISU_JD import LISUJD
from LISU_SP import LISUSP
from LISU_WD import LISUWD
#from LISU_2D import LISU2D

# Nota: Por ahora, dejalo directo, pero se reuiere ligarlo con la ontologia y para ello necesitas la cadena
#LISUDV = []

#def setDaemon(i):
#    switcher={
#        'SL-6632 Dark Tornado Joystick':Thread(target = LISUJD).start(),
#        '3Dconnexion KMJ Emulator':Thread(target = LISUSP).start(),
#        '4 axis 4 button ':Thread(target = LISUWD).start()
#        }
#    return switcher.get(i,"No device connected")

def checkDevices():
    #print 'Checking devices...'
    pygame.init()
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
    print "LISU has detected " + str(joystick_count) + ' devices...'
    print "Checking ontology..."
    print "Getting transfer functions..."

    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)        
        joystick.init()
        #print joystick.get_name() + " is joystick " + str(i)

        #Getting attributes
        #LISUDV.append([i, joystick.get_name(), joystick.get_numaxes()])
        #setDaemon(joystick.get_name())
        if joystick.get_name() == 'SL-6632 Dark Tornado Joystick':
            print 'Initiating and setting up SL-6632 Dark Tornado Joystick...'
            Thread(target = LISUJD, args=(i,)).start()
        elif joystick.get_name() == '3Dconnexion KMJ Emulator':
            print 'Initiating and setting up 3Dconnexion KMJ Emulator...'
            Thread(target = LISUSP).start()
        elif joystick.get_name() == '4 axis 4 button ':
            print 'Initiating and setting up 4 axis 4 button...'
            Thread(target = LISUWD, args=(i,)).start()

    print "Getting last updates..."
    print "Mapping transfer functions..."
    
  
if __name__ == '__main__':
    try:
        checkDevices()
    except KeyboardInterrupt:
        sys.exit()
    
   
