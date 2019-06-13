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
import A_star_search
import World_Generator


MAX, MIN = 1000, -1000 
pitfall = World_Generator.Genpitfall()
claywall = World_Generator.Genclaywall()
lava = World_Generator.Genlava()
highwall = World_Generator.Genhighwall()
complicate = World_Generator.complicate_map()
normal = World_Generator.normal_map()
agent_position = [0.5,0.5] #[x,z]
destination = [58.5,58.5]#[x,z]

map1 = '''
    <DrawingDecorator>
        <DrawBlock x="0" y="4" z="0" type="quartz_block" />
        <DrawBlock x="58" y="4" z="58" type="redstone_block" />
        <DrawCuboid x1="-1" y1="4" z1="-1" x2="59" y2="10" z2="-1" type="gold_block"/>
        <DrawCuboid x1="-1" y1="4" z1="-1" x2="-1" y2="10" z2="59" type="gold_block"/>
        <DrawCuboid x1="59" y1="4" z1="59" x2="-1" y2="10" z2="59" type="gold_block"/>
        <DrawCuboid x1="59" y1="4" z1="59" x2="59" y2="10" z2="-1" type="gold_block"/> 
    </DrawingDecorator>
'''

map2 = '''
    <DrawingDecorator>
        <DrawBlock x="0" y="4" z="0" type="quartz_block" />
        <DrawBlock x="58" y="4" z="58" type="redstone_block" />
        <DrawCuboid x1="-1" y1="4" z1="-2" x2="59" y2="10" z2="-2" type="gold_block"/>
        <DrawCuboid x1="-1" y1="4" z1="-1" x2="-1" y2="10" z2="59" type="gold_block"/>
        <DrawCuboid x1="59" y1="4" z1="59" x2="-1" y2="10" z2="59" type="gold_block"/>
        <DrawCuboid x1="59" y1="4" z1="59" x2="59" y2="10" z2="-1" type="gold_block"/>
        '''+normal+'''
        
    </DrawingDecorator>
'''

def get_grid(world_state):
    while world_state.is_mission_running:
        time.sleep(0.1)
        world_state = agent_host.getWorldState()
        if len(world_state.errors) > 0:
            raise AssertionError('Could not load grid.')

        if world_state.number_of_observations_since_last_state > 0:
            msg = world_state.observations[-1].text
            ob = json.loads(msg)
            full_grid = ob.get(u'floorAll', 0)
            break
    
    return full_grid

def GetMissionXML( mazeblock, agent_host ):
    return '''<?xml version="1.0" encoding="UTF-8" ?>
    <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <About>
            <Summary>Run our basic Adventure Map!</Summary>
        </About>
        
        <ModSettings>
            <MsPerTick>''' + str(50) + '''</MsPerTick>
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
                <ServerQuitWhenAnyAgentFinishes />
            </ServerHandlers>
        </ServerSection>

        <AgentSection mode="Survival">
            <Name>StupidAI(A)</Name>
            <AgentStart>
                <Placement x="0.5" y="5" z="0.5"/>
            </AgentStart>
            <AgentHandlers>
                 
                 <DiscreteMovementCommands/>
                <AgentQuitFromTouchingBlockType>
                    <Block type="redstone_block"/>
                </AgentQuitFromTouchingBlockType>

                <ChatCommands> </ChatCommands>
                <ObservationFromFullStats/>



                
                <ObservationFromGrid>
                      <Grid name="floorAll">
                        <min x="0" y="-1" z="0"/>
                        <max x="58" y="-1" z="58"/>
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
    
    full_grid = get_grid(world_state)    
    route = A_star_search.astar_search(full_grid)
    for i in route:
        print("route: " + str(i.position))
    action_list = A_star_search.get_actions(route)
    index = 0
    # main loop:
    #agent_position = [0.5,0.5]
    if world_state.is_mission_running:
        agent_host.sendCommand('chat /difficulty hard')
    while world_state.is_mission_running:
        time.sleep(0.1)        
        if index >= len(action_list):
            print("Error:", "out of actions, but mission has not ended!")
            time.sleep(2)
        else:
            agent_host.sendCommand(action_list[index])
            agent_host.sendCommand('chat /effect @p 17 1 10')
            time.sleep(1)
        index += 1
        if len(action_list) == index:
            time.sleep(2)
        world_state = agent_host.getWorldState()
        
        
    print("total steps: " + str(len(action_list)))
    print("Mission has stopped.")
    time.sleep(0.5) # Give mod a little time to get back to dormant state.
