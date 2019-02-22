######## BEGINING OF THE DAEMON ######################################################
######## LIBRARIES ###################################################################
import socket
import time
#import stopwatch
import pygame
from pygame.locals import *
import os

######################################################################################
######## VARIABLES  ##################################################################
st1 = time.time()
rotr = 0
rotp = 0
roty = 0

i = 0
ejex = 0
ejey = 0
ejez = 0 #0.05

sigmaX = 0.057818 # With seven: 0.115637 # Originally: 0.008858 
sigmaY = 0.054186 # With seven: 0.108371 # Originally: 0.002811 
sigmaZ = 0.00507237109378 # With seven: 0.119617 # Originally: 0.009863 
#sigmaX = 0.059 # With seven: 0.115637 # Originally: 0.008858 
#sigmaY = 0.055 # With seven: 0.108371 # Originally: 0.002811 
#sigmaZ = 0.9008 # With seven: 0.119617 # Originally: 0.009863 

sigmas = {
    'x': sigmaX,
    'y': sigmaY,
    'z': sigmaZ
}



#Connecting to the port used by DRISHTI
s = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
host = 'localhost'
port = 7755
s.connect((host, port))
pygame.init()

# Used to manage how fast the screen updates
TestSubj        = 1
TestSubj2       = 1
done            = False
clock           = pygame.time.Clock()
c               = pygame.time.Clock()
joystick_count  = pygame.joystick.get_count()
st1             = time.time ();
last_fps        = 0
#current         = win32api.GetCursorPos()
last            = time.time()

# Function definition is here
global xValues
xValues = []
global yValues
yValues = []
global zValues
zValues = []
global vStpwatch
vStpwatch = []

global xValWING
xValWING = []
global yValWING
yValWING = []
global zValWING
zValWING = []
global vTimeWING
vTimeWING = []

global xValMOUSE
xValMOUSE = []
global yValMOUSE
yValMOUSE = []
global vTimeMOUSE
vTimeMOUSE = []
global vTicksMOUSE
vTicksMOUSE = []

#Stopwatch
#stpwtch = stopwatch.Timer()

######################################################################################
######## FUNCTIONS  ##################################################################
def AjusteEjes(limite, eje, tipo_eje):    

    #varAuxiliar = ejes[tipo_eje]
    #print ("Limite = " + str(limite))
    varAuxiliar = limite
    sigma = sigmas[tipo_eje]

    varAuxiliar = varAuxiliar + sigma
    
    if eje < 0:
        #print ("Checa si es negativo. Eje = " + str(eje))
        varAuxiliar = -1 * varAuxiliar
            
    if eje > 0 and eje <= varAuxiliar:        
        #print ("Es mayor a cero. Eje = " + str(eje))
        eje = 0
    elif  eje  < 0 and eje >= varAuxiliar:
        #print ("Si es negativo. Eje = " + str(eje))
        eje = 0

    elif  eje == 0:
        eje = 0

    #print ("Nuevo WING " + tipo_eje + " = " + str(eje))
    return eje
    

def saveAxisValues(x, y, z, v):    
    xValues.append(x)
    yValues.append(y)
    zValues.append(z)
    vStpwatch.append(v)

def saveAxisValWING(x, y, z, v):    
    xValWING.append(x)
    yValWING.append(y)
    zValWING.append(z)
    vTimeWING.append(v)

def saveAxisValMOUSE(x, y, t):    
    xValMOUSE.append(x)
    yValMOUSE.append(y)
    vTicksMOUSE.append(t)
    

def save2plotValuesDRISHTI(TestSubj, stpwtch):        
    path = 'C:/Users/sandovam/Documents/Experiment Results/Participant' + str(TestSubj) + '/DRISHTI'
    os.makedirs(path, exist_ok=True)

    target = open (path + "/" + "x_values.txt", 'a')
    target.write(','.join(str(e) for e in xValues))
    target.close()
        
    target = open (path + "/" + "y_values.txt", 'a')
    target.write(','.join(str(e) for e in yValues))
    target.close()

    target = open (path + "/" + "z_values.txt", 'a')
    target.write(','.join(str(e) for e in zValues))
    target.close()

    target = open (path + "/" + "time_values.txt", 'a')
    target.write(','.join(str(e) for e in vStpwatch))
    target.close()

    target = open (path + "/" + "exp_time_values.txt", 'a')
    target.write(str(stpwtch) + " seconds for all the experimental test" )
    target.close()

def save2plotValuesWING(TestSubj, stpwtch):        
    path = 'C:/Users/sandovam/Documents/Experiment Results/Participant' + str(TestSubj) + '/WING'
    os.makedirs(path, exist_ok=True)

    target = open (path + "/" + "x_values.txt", 'a')
    target.write(','.join(str(e) for e in xValWING))
    target.close()
        
    target = open (path + "/" + "y_values.txt", 'a')
    target.write(','.join(str(e) for e in yValWING))
    target.close()

    target = open (path + "/" + "z_values.txt", 'a')
    target.write(','.join(str(e) for e in zValWING))
    target.close()

    target = open (path + "/" + "time_values.txt", 'a')
    target.write(','.join(str(e) for e in vTimeWING))
    target.close()

    target = open (path + "/" + "exp_time_values.txt", 'a')
    target.write(str(stpwtch) + " seconds seconds for all the experimental test" )
    target.close()

def save2plotValuesMOUSE(TestSubj, stpwtch):        
    path = 'C:/Users/sandovam/Documents/Experiment Results/Participant' + str(TestSubj) + '/MOUSE'
    os.makedirs(path, exist_ok=True)

    target = open (path + "/" + "x_values.txt", 'a')
    target.write(','.join(str(e) for e in xValMOUSE))
    target.close()
        
    target = open (path + "/" + "y_values.txt", 'a')
    target.write(','.join(str(e) for e in yValMOUSE))
    target.close()
    
    target = open (path + "/" + "mouse_ticks_values.txt", 'a')
    target.write(','.join(str(e) for e in vTicksMOUSE))
    target.close()

    target = open (path + "/" + "exp_time_values.txt", 'a')
    target.write(str(stpwtch) + " seconds seconds for all the experimental test" )
    target.close()

######################################################################################
######## MAIN FUNCTION ###############################################################
if joystick_count == 0:
    # No joysticks!
    print ("Error, no se detecto ningun joystick!")
else:
    # Use joystick #0 and initialize it
    wing_joystick = pygame.joystick.Joystick(0)
    wing_joystick.init()
    if joystick_count > 1:
        second_joystick = pygame.joystick.Joystick(1)
        second_joystick.init()
        if second_joystick.get_init() == 1: print ("Joystick detectado")

if wing_joystick.get_init() == 1: print ("Wing detectado")


#j = 1

while not done:
#while j < 200:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        c.tick()
        if pygame.time.get_ticks() - last_fps > 1000:
            #print ("FPS: ", c.get_fps())
            last_fps = pygame.time.get_ticks()

                      
        if joystick_count != 0:             
            # This gets the position of the axis on the game controller. It returns a number between -1.0 and +1.0
            # However, for some reason x always returns a +1.0
            x_axis_pos = wing_joystick.get_axis(0) 
            y_axis_pos = wing_joystick.get_axis(1)
            z_axis_pos = wing_joystick.get_axis(3)

            if i == 0:
                ejex = ejex + x_axis_pos
                ejey = ejey + y_axis_pos
                ejez = ejez + z_axis_pos
                
                print ("Limite X= [-" + str(ejex + sigmas["x"]) + ", " + str(ejex + sigmas["x"]) + "]")
                print ("Limite Y= [-" + str(ejey + sigmas["y"]) + ", " + str(ejey + sigmas["y"]) + "]")
                print ("Limite Z= [-" + str(ejez + sigmas["z"]) + ", " + str(ejez + sigmas["z"]) + "]")

            ejes = {
                'x': ejex,
                'y': ejey,
                'z': ejez
            }

            i = i + 1
            
            # Saving raw values          
            #saveAxisValWING(x_axis_pos, y_axis_pos, z_axis_pos, pygame.time.get_ticks())

            #Filter
            x_axis_pos = AjusteEjes(ejes["x"], x_axis_pos, "x")            
            y_axis_pos = AjusteEjes(ejes["y"], y_axis_pos, "y")            
            z_axis_pos = AjusteEjes(ejes["z"], z_axis_pos, "z")            
                                    
            # Rotate x and y according to the axis. Then, they are multiplied by 10 to speed up the movement.
            rotr = rotr + (x_axis_pos * 10)
            rotp = rotp + (y_axis_pos * 10)
            roty = roty + (z_axis_pos * 10)
            
            # Saving the values in an array and display
            # time.time()-st1) / 0.01 - time taken to complete a round trip to a server using TCP in min            
            if (rotr!=0 or rotp != 0 or roty != 0) and ((time.time() - st1) > 0.15 ):
                
                rotAngle = abs(round((rotr + rotp + roty)))                
                #saveAxisValues(x_axis_pos, y_axis_pos, z_axis_pos, pygame.time.get_ticks())
                # 1 is DEG2RAD(angle): angle * PI / 180.0                                
                multipacket = 'addrotation %s %s %s %s' %(rotr, rotp, roty, (rotAngle))
                s.send(multipacket.encode('utf-8'))              
                
                rotr = 0
                rotp = 0
                roty = 0
                st1 = time.time ();
        
            
        clock.tick(60)
        #j = j + 1
                
pygame.quit()
######## ENDING OF THE DAEMON ########################################################
