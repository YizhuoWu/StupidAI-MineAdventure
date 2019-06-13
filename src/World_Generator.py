from __future__ import print_function
from builtins import range
import MalmoPython
import os
import random
import sys
import time
import datetime
import json
import random
import malmoutils

malmoutils.fix_print()

agent_host = MalmoPython.AgentHost()
malmoutils.parse_command_line(agent_host)
recordingsDirectory = malmoutils.get_recordings_directory(agent_host)
video_requirements = '<VideoProducer><Width>860</Width><Height>480</Height></VideoProducer>' if agent_host.receivedArgument("record_video") else ''

def GenCuboid(x1, y1, z1, x2, y2, z2, blocktype,color):
    if color == "":
        return '<DrawCuboid x1="' + str(x1) + '" y1="' + str(y1) + '" z1="' + str(z1) + '" x2="' + str(x2) + '" y2="' + str(y2) + '" z2="' + str(z2) + '" type="' + blocktype + '"/>'
    else:
        return '<DrawCuboid x1="' + str(x1) + '" y1="' + str(y1) + '" z1="' + str(z1) + '" x2="' + str(x2) + '" y2="' + str(y2) + '" z2="' + str(z2) + '" type="' + blocktype + '" colour="'+color+'"/>'
    
def Genpitfall():
    pitfall = ""
    pit_number = random.randint(5, 15)
    for i in range(pit_number):
        sizex = random.randint(1,5)
        sizez = random.randint(1,5)
        startx = random.randint(0,58)
        startz = random.randint(0,58)
        pitfall += GenCuboid (startx,4,startz,startx+sizex,4,startz+sizez,"air","")
    return pitfall
    
def Genclaywall():
    clay_number = random.randint(5, 15)
    clay=""
    for i in range(clay_number):
        startx = random.randint(1,57)
        startz = random.randint(1,57)
        sizex = random.randint(0,15)
    
        if sizex == 0:
            sizez = random.randint(1,15)
        else:
            sizez = 0
    
    color = random.sample(["WHITE", "ORANGE", "MAGENTA","LIGHT_BLUE","LIME", "PINK", "GRAY","CYAN","PURPLE","BLUE","BROWN","RED","BLACK"],1)
    clay += GenCuboid (startx,4,startz,startx+sizex,5,startz+sizez,"stained_hardened_clay",color[0])

    return clay

def Genlava():
    lava = ""
    '''
    lava_number = random.randint(3, 5)
        
    for i in range(lava_number):
        sizex = random.randint(1,5)
        sizez = random.randint(1,5)
        startx = random.randint(1,57)
        startz = random.randint(1,57)
        if (startx == 0 and startz == 0) or (startx == 58 and startz == 58) :
             startx = random.randint(1,57)
             startz = random.randint(1,57)
        
        if startx+sizex >= 58 and startz+sizez >= 58:
            lava += GenCuboid (startx,4,startz,57,4,57,"lava","")
        else:
            lava += GenCuboid (startx,4,startz,startx+sizex,4,startz+sizez,"lava","")
    '''
    lava += GenCuboid (2,4,0,4,4,5,"lava","")
    lava += GenCuboid (1,4,5,7,4,10,"lava","")
    lava += GenCuboid (0,4,1,0,4,2,"lava","")
    lava += GenCuboid (0,4,20,35,4,30,"lava","")
    lava += GenCuboid (37,4,20,58,4,30,"lava","")
    lava += GenCuboid (1,4,32,58,4,57,"lava","")
    return lava

def Genhighwall():
    
    high_wall_number = random.randint(4, 7)
    high_wall = ""
    for i in range(high_wall_number):    
        startx = random.randint(1,57)
        startz = random.randint(1,57)
        sizex = random.randint(0,15)
        y = random.randint(7,10)
        if sizex == 0:
            sizez = random.randint(5,15)
            if 58-startz > 28:
                high_wall += GenCuboid (startx,4,startz,startx,y,startz-sizez,"iron_block","")
            else:
                high_wall += GenCuboid (startx,4,startz,startx,y,startz+sizez,"iron_block","")
                
            
        else:
            sizez = 0
            if 58-startx > 28:
                high_wall += GenCuboid (startx,4,startz,startx-sizex,y,startz,"iron_block","")
            else:
                high_wall += GenCuboid (startx,4,startz,startx+sizex,y,startz,"iron_block","")
    return high_wall
def complicate_map():
    complicate = ""
    complicate += GenCuboid (0,4,15,20,9,15,"iron_block","")
    complicate += GenCuboid (7,4,3,30,9,3,"iron_block","")
    complicate += GenCuboid (44,4,2,44,9,19,"iron_block","")
    complicate += GenCuboid (44,4,7,35,9,7,"iron_block","")
    complicate += GenCuboid (52,4,58,52,9,54,"iron_block","")
    complicate += GenCuboid (44,4,-1,40,4,8,"lava","")
    complicate += GenCuboid (2,4,-1,4,4,5,"lava","")
    complicate += GenCuboid (1,4,5,6,4,10,"lava","")
    complicate += GenCuboid (0,4,1,0,4,2,"lava","")
    complicate += GenCuboid (0,4,20,8,4,30,"lava","")
    complicate += GenCuboid (10,4,20,35,4,30,"lava","")
    complicate += GenCuboid (37,4,20,58,4,30,"lava","")
    complicate += GenCuboid (8,4,45,58,4,49,"leaves","")
    for i in range(10,59,2):
        complicate += GenCuboid (i,4,47,i,6,47,"log","")
        complicate += GenCuboid (i+2,6,47,i-2,6,47,"leaves","")
        complicate += GenCuboid (i+1,7,47,i-1,7,47,"leaves","")
        complicate += GenCuboid (i,8,47,i,8,47,"leaves","")
        complicate += GenCuboid (i,6,45,i,6,49,"leaves","")
        complicate += GenCuboid (i,7,46,i,7,48,"leaves","")
    complicate += GenCuboid (25,2,35,40,4,42,"water","")
    complicate += GenCuboid (33,2,58,26,4,56,"water","")
    complicate += GenCuboid (28,2,54,26,4,56,"water","")
    complicate += GenCuboid (32,2,53,43,4,50,"water","")
    complicate += GenCuboid (38,2,53,37,4,56,"water","")
    complicate += GenCuboid (13,2,50,17,4,56,"water","")
    return complicate
    
def normal_map():
    normal = ""
    normal += GenCuboid (15,2,16,35,4,25,"water","")
    normal += GenCuboid (0,2,40,35,4,45,"lava","")
    normal += GenCuboid (2,4,8,16,4,13,"leaves","")
    normal += GenCuboid (2,4,-1,4,4,5,"lava","")
    normal += GenCuboid (0,4,1,0,4,2,"lava","")
    normal += GenCuboid (0,4,48,15,9,48,"iron_block","")
    normal += GenCuboid (55,4,40,44,4,44,"lava","")
    normal += GenCuboid (32,4,53,43,4,50,"lava","")
    normal += GenCuboid (38,4,53,37,4,56,"lava","")
    normal += GenCuboid (55,2,-1,45,4,16,"water","")
    normal += GenCuboid (50,4,58,50,9,54,"iron_block","")

    
    
    for i in range(4,15,2):
        normal += GenCuboid (i,4,10,i,6,10,"log","")
        normal += GenCuboid (i+2,6,10,i-2,6,10,"leaves","")
        normal += GenCuboid (i+1,7,10,i-1,7,10,"leaves","")
        normal += GenCuboid (i,8,10,i,8,10,"leaves","")
        normal += GenCuboid (i,6,8,i,6,12,"leaves","")
        normal += GenCuboid (i,7,9,i,7,11,"leaves","")
    normal += GenCuboid (6,2,-1,10,4,5,"water","")
    return normal
