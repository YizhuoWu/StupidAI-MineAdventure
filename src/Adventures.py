from __future__ import print_function
from builtins import range
import MalmoPython
import os
import random
import sys
import time
import json
import errno
import malmoutils

malmoutils.fix_print()

agent_host = MalmoPython.AgentHost()
agent_host.addOptionalIntArgument( "speed,s", "Length of tick, in ms.",1)
malmoutils.parse_command_line(agent_host)

adventure_map_1 = '''
    <MazeDecorator>
        <SizeAndPosition length="60" width="60" yOrigin="225" zOrigin="0" height="180"/>
        <GapProbability variance="1">0.5</GapProbability>
        <Seed>random</Seed>
        <MaterialSeed>random</MaterialSeed>
        <AllowDiagonalMovement>false</AllowDiagonalMovement>
        <StartBlock fixedToEdge="true" type="emerald_block" height="1"/>
        <EndBlock fixedToEdge="true" type="redstone_block diamond_block gold_block" height="12"/>
        <PathBlock type="stained_hardened_clay" colour="WHITE ORANGE MAGENTA LIGHT_BLUE YELLOW LIME PINK GRAY SILVER CYAN PURPLE BLUE BROWN GREEN RED " height="1"/>
        <FloorBlock type="stone"/>
        <GapBlock type="stone"/>
        <AddQuitProducer description="finished maze"/>
        <AddNavigationObservations/>
    </MazeDecorator>
'''

def GetMissionXML(mazeblock,agent_host):
    return '''<?xml version="1.0" encoding="UTF-8" ?>
    <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <About>
            <Summary>Run the maze!</Summary>
        </About>
        
        <ModSettings>
            <MsPerTick>''' + str(TICK_LENGTH) + '''</MsPerTick>
        </ModSettings>

        <ServerSection>
            <ServerInitialConditions>
                <AllowSpawning>false</AllowSpawning>
            </ServerInitialConditions>
            <ServerHandlers>
                <FlatWorldGenerator generatorString="3;7,220*1,5*3,2;3;,biome_1" />
                ''' + mazeblock + '''
                <ServerQuitFromTimeUp timeLimitMs="45000"/>
                <ServerQuitWhenAnyAgentFinishes />
            </ServerHandlers>
        </ServerSection>

        <AgentSection mode="Survival">
            <Name>James Bond</Name>
            <AgentStart>
                <Placement x="-204" y="81" z="217"/>
            </AgentStart>
            <AgentHandlers>
                <ContinuousMovementCommands turnSpeedDegs="840">
                    <ModifierList type="deny-list"> <!-- Example deny-list: prevent agent from strafing -->
                        <command>strafe</command>
                    </ModifierList>
                </ContinuousMovementCommands>''' + malmoutils.get_video_xml(agent_host) + '''
                </AgentHandlers>
        </AgentSection>

    </Mission>'''


validate =True
agent_host.setObservationsPolicy(MalmoPython.ObservationsPolicy.LATEST_OBSERVATION_ONLY)
TICK_LENGTH = agent_host.getIntArgument("speed")
my_mission_record = malmoutils.get_default_recording_object(agent_host, "Mission 1")
my_mission = MalmoPython.MissionSpec(GetMissionXML(adventure_map_1,agent_host),validate)


agent_host.startMission(my_mission,my_mission_record)
