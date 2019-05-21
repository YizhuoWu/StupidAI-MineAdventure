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
    
    color = random.sample(["WHITE", "ORANGE", "MAGENTA","LIGHT_BLUE","LIME", "PINK", "GRAY","CYAN","PURPLE","BLUE","BROWN","GREEN","RED","BLACK"],1)
    clay += GenCuboid (startx,5,startz,startx+sizex,5,startz+sizez,"stained_hardened_clay",color[0])

    return clay

def Genlava():
    lava = ""
    lava_number = random.randint(5, 10)
        
    for i in range(lava_number):
        sizex = random.randint(1,5)
        sizez = random.randint(1,5)
        startx = random.randint(5,57)
        startz = random.randint(5,57)
        y = random.randint(2,4)
        lava += GenCuboid (startx,y,startz,startx+sizex,y,startz+sizez,"lava","")

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
                high_wall += GenCuboid (startx,5,startz,startx,y,startz-sizez,"iron_block","")
            else:
                high_wall += GenCuboid (startx,5,startz,startx,y,startz+sizez,"iron_block","")
                
            
        else:
            sizez = 0
            if 58-startx > 28:
                high_wall += GenCuboid (startx,5,startz,startx-sizex,y,startz,"iron_block","")
            else:
                high_wall += GenCuboid (startx,5,startz,startx+sizex,y,startz,"iron_block","")
    return high_wall
