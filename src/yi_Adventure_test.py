from __future__ import print_function
# ------------------------------------------------------------------------------------------------
# Copyright (c) 2016 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# ------------------------------------------------------------------------------------------------

from builtins import range
import MalmoPython
import os
import random
import sys
import time
import json
import errno
import malmoutils
import yi_Algorithm
import World_Generator



MAX, MIN = 1000, -1000 
pitfall = World_Generator.Genpitfall()
claywall = World_Generator.Genclaywall()
lava = World_Generator.Genlava()
highwall = World_Generator.Genhighwall()
##agent_host = MalmoPython.AgentHost()
##agent_host.addOptionalIntArgument( "speed,s", "Length of tick, in ms.", 50)
##malmoutils.parse_command_line(agent_host)

map1 = '''
    <DrawingDecorator>
        <DrawBlock x="0" y="4" z="0" type="quartz_block" />
        <DrawBlock x="58" y="4" z="58" type="redstone_block" />
        <DrawCuboid x1="-1" y1="5" z1="-1" x2="59" y2="10" z2="-1" type="gold_block"/>
        <DrawCuboid x1="-1" y1="5" z1="-1" x2="-1" y2="10" z2="59" type="gold_block"/>
        <DrawCuboid x1="59" y1="5" z1="59" x2="-1" y2="10" z2="59" type="gold_block"/>
        <DrawCuboid x1="59" y1="5" z1="59" x2="59" y2="10" z2="-1" type="gold_block"/> 
    </DrawingDecorator>
'''

map2 = '''
    <DrawingDecorator>
        <DrawBlock x="0" y="4" z="0" type="quartz_block" />
        <DrawBlock x="58" y="4" z="58" type="redstone_block" />
        <DrawCuboid x1="-1" y1="5" z1="-1" x2="59" y2="10" z2="-1" type="gold_block"/>
        <DrawCuboid x1="-1" y1="5" z1="-1" x2="-1" y2="10" z2="59" type="gold_block"/>
        <DrawCuboid x1="59" y1="5" z1="59" x2="-1" y2="10" z2="59" type="gold_block"/>
        <DrawCuboid x1="59" y1="5" z1="59" x2="59" y2="10" z2="-1" type="gold_block"/>
        '''+claywall+'''
    </DrawingDecorator>
'''

def GetMissionXML( mazeblock, agent_host ):
    return '''<?xml version="1.0" encoding="UTF-8" ?>
    <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <About>
            <Summary>Run our basic Adventure Map!</Summary>
        </About>
        
        <ModSettings>
            <MsPerTick>''' + str(35) + '''</MsPerTick>
        </ModSettings>

        <ServerSection>
            <ServerInitialConditions>
                <Time>
                    <StartTime>1000</StartTime>
                    <AllowPassageOfTime>false</AllowPassageOfTime>
                </Time>
                <Weather>clear</Weather>
                <AllowSpawning>false</AllowSpawning>
            </ServerInitialConditions>
            <ServerHandlers>
                <FlatWorldGenerator generatorString="3;1*minecraft:lava,1*minecraft:bedrock,1*minecraft:ice,1*minecraft:dirt,1*minecraft:grass" />
                ''' + mazeblock + '''
                <ServerQuitFromTimeUp timeLimitMs="450000"/>
                <ServerQuitWhenAnyAgentFinishes />
            </ServerHandlers>
        </ServerSection>

        <AgentSection mode="Survival">
            <Name>James Bond</Name>
            <AgentStart>
                <Placement x="0.5" y="5" z="0.5"/>
            </AgentStart>
            <AgentHandlers>
                <ContinuousMovementCommands turnSpeedDegs="840"/>
                <AgentQuitFromTouchingBlockType>
                    <Block type="redstone_block"/>
                </AgentQuitFromTouchingBlockType>

                <ChatCommands> </ChatCommands>
                <ObservationFromFullStats/>



                
                <ObservationFromGrid>
                    <Grid name="floor3x3">
                        <min x="-1" y="-1" z="-1"/>
                        <max x="1" y="0" z="1"/>
                    </Grid>
                </ObservationFromGrid>

                </AgentHandlers>
        </AgentSection>

    </Mission>'''

validate = True
mazeblocks = [map2]

#agent_host.setObservationsPolicy(MalmoPython.ObservationsPolicy.LATEST_OBSERVATION_ONLY)

##if agent_host.receivedArgument("test"):
##    num_reps = 10
##else:
##    num_reps = 30000

##TICK_LENGTH = agent_host.getIntArgument("speed")

for iRepeat in range(10):
    pitfall = World_Generator.Genpitfall()
    claywall = World_Generator.Genclaywall()
    lava = World_Generator.Genlava()
    highwall = World_Generator.Genhighwall()
    malmoutils.fix_print()

    agent_host = MalmoPython.AgentHost()
##    agent_host.addOptionalIntArgument( "speed,s", "Length of tick, in ms.", 50)
    malmoutils.parse_command_line(agent_host)
    


    
    my_mission_record = malmoutils.get_default_recording_object(agent_host, "Mission 1")
    mazeblock = random.choice(mazeblocks)
    my_mission = MalmoPython.MissionSpec(GetMissionXML(mazeblock, agent_host),validate)

    my_mission.requestVideo(800, 500)
    my_mission.setViewpoint(1)




    max_retries = 3
    for retry in range(max_retries):
        try:
            agent_host.startMission( my_mission, my_mission_record )

            break
        except RuntimeError as e:
            if retry == max_retries - 1:
                print("Error starting mission:",e)
                exit(1)
            else:
                time.sleep(2)

    print("Waiting for the mission to start", end=' ')
    world_state = agent_host.getWorldState()
    while not world_state.has_mission_begun:
        print(".", end="")
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        if len(world_state.errors):
            print()
            for error in world_state.errors:
                print("Error:",error.text)
                exit()
    print()

    # main loop:
    if world_state.is_mission_running:
        agent_host.sendCommand('chat /difficulty hard')
        agent_host.sendCommand('chat /effect @p 17 15 20')
    while world_state.is_mission_running:

        #agent_host.sendCommand('chat /difficulty hard')
        #agent_host.sendCommand('chat /effect @p 17 15 20')





        
        time.sleep(0.5)
        world_state = agent_host.getWorldState()


        if world_state.number_of_observations_since_last_state > 0:

            msg = world_state.observations[-1].text
            ob = json.loads(msg)

            print("Hunger Val: "+ str(ob["Food"]))
            grid = ob.get(u'floor3x3', 0)

            base_grid = grid[0:9]
            block_grid = grid[9:]
            print("base grid:" + str(base_grid))
            print("block grid:" + str(block_grid))

            num_list = yi_Algorithm.observation_to_nums(block_grid,base_grid)
            print(num_list)
            max_value = yi_Algorithm.minimax(0, 0, True, num_list, MIN, MAX)
            print("val")
            print(max_value)
            if num_list.count(max_value)>1:

                index = yi_Algorithm.find_best_index(num_list,max_value)
            else:
                index = num_list.index(max_value)
            print("best index: ")
            print(index)
            yi_Algorithm.make_action(index,agent_host)



    print("Mission has stopped.")
    time.sleep(0.5) # Give mod a little time to get back to dormant state.
