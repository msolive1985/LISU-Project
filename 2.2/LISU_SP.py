"""LISU_SP.py: Reads a joystick device using pygame and sends the information via UDP."""
__author__ = "Mario Sandoval"
__copyright__ = "Copyright 2018"
__license__ = "The University of Manchester"
__version__ = "2.2.1"
__maintainer__ = "Mario Sandoval"
__email__ = "mario.sandovalolive@manchester.ac.uk"
__status__ = "Development"

import spacenavigator, socket, struct, time
import pygame, random, sys, logging
import datetime
from modules.utils import *

def LISUSP():
    #currentDT = datetime.datetime.now()
    #record = currentDT.year + currentDT.month + currentDT.day
    #logging.basicConfig(filename=("lisu_log_sp.txt"), level=logging.DEBUG, format='%(asctime)s, %(message)s')
    with open("LISU_6DOF.txt", "r") as ins:
        array = []
        for line in ins:
            array.append(line)

    UDP_IP = "127.0.0.1"
    camera_port = 7755
    bricks_port = 7775
    update_rate = 0.55
    array_index = 0
    time_movement = 0.0
    packet = ""
    mapped_func = array[array_index] 
        
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
            roll     = state.roll
            pitch    = state.pitch
            yaw      = state.yaw

            if state.button == 1:
                array_index = array_index + 1                
                if array_index >= len(array):
                    array_index = 0
                mapped_func = array[array_index]
                print "LISU changed mode to:" + mapped_func.rstrip()

            if mapped_func.rstrip() == "addrotation":
                time_movement = update_rate
                mapped_comp = str(abs(round(((roll + pitch + yaw)/3) * 75)))
                UDP_PORT = camera_port
                packet = mapped_func.rstrip() + " " + str(round(roll,2)) + " " + str(round(pitch,2)) + " " + str(round(yaw,2)) + " " + mapped_comp                            
            else:
                time_movement = 1
                UDP_PORT = bricks_port
                if mapped_func.rstrip() == "rotation_angle":
                    mapped_comp = str(round(pitch,2) * 180)
                    packet = mapped_func.rstrip() + " " + mapped_comp
                else:
                    packet = mapped_func.rstrip() + " " + str(round(roll,2)) + " " + str(round(pitch,2)) + " " + str(round(yaw,2))

                                    
            if(roll!=0.0 or pitch != 0.0 or yaw != 0.0):
                if mapped_func.rstrip() == "adjust_calibration":
                    f= open("calibration.txt","w+")
                    print "calibration: " + str(round(yaw,2) * 0.75)
                    f.write(str(round(yaw,2) * 0.75))
                    f.close()
                elif mapped_func.rstrip() == "update_timer":
                    f= open("update_timer.txt","w+")
                    print "update_timer: " + str(round(yaw,2))
                    f.write(str(round(yaw,2) * 0.85))
                    f.close()
                else:
                    print packet
                    sock.sendto(packet, (UDP_IP, UDP_PORT))
                    logging.info(packet)
                    time.sleep(time_movement)                
                
                #print packet
                #print mapped_func.rstrip() + " " + str(round(roll,2)) + " " + str(round(pitch,2)) + " " + str(round(yaw,2))                
                #packet = "bricks_translate " + str(round(roll,2)) + " " + str(round(pitch,2)) + " " + str(round(yaw,2))
                #sock.sendto(packet, (UDP_IP, UDP_PORT))
                #logging.info("bricks_translate," + str(round(roll,2)) + "," + str(round(pitch,2)) + "," + str(round(yaw,2)))
                #time.sleep(0.5)
      
            while elapsed < update_rate:
                elapsed = time.time() - current       

if __name__ == "__main__":
    LISUSP()
