---
layout: default
title: Proposal
---


# 2.2 Summary of the Project


The project is going to be an adventure game for our agent. In the project, there will be a randomly generated adventure map for our agent, 
the goal of our agent is to leave this “dangerous” area as soon as possible, in other words, our agent should use AI/ML algorithms to find a best way to leave this map(arrive at exit). 
The input of the project can be divided into two parts. The first part is the outside environment input. This means we need to give the project several attributes. 
This contains, but not limited to size of the map, the layout of the map, the entities in the map, the position of the beasts, the solution of the map and other attributes of the map. 
The second part of the input is the configuration of the agent itself. These inputs will be the HP value of the agent, the speed of the agent, the weapon that the agent will take and other detail attributes of the agent. 
The final output, in the program/code level, will be an action array which contains the actions the agent will take during the whole game process. 
In the game/visual level, the output will be that the agent can successfully finish the map with lowest cost. 

# 2.3 AI/ML Algorithms

The project will combine the A* search algorithm and alpha-beta pruning algorithm for our project to generate the actions for the agent, 
we will also build a knowledge-based smart AI to perform the task.

# 2.4 Evaluation Plan

The success of the project means our agent move out of the map. The base requirement is the agent must be alive during the whole game process…

Metric: 
Baselines: 
Use Algorithms to generate a solution list of actions then push the actions to agent; or agent takes each step immediately calculated by internals of the algorithm.
Sanity cases: 
Moonshot case: 
Visualize the internals of the algorithm: Draw a 2D map to show all the objects in our game state and also set a counter to track our agent’s HP. 
