---
layout: default
title: Proposal
---

# 2.2 Summary of the Project

The project is going to be an adventure game for our agent. In the project, there will be a randomly generated adventure map for our agent, 
the goal of our agent is to leave this “dangerous” area as soon as possible, in other words, our agent should use AI/ML algorithms to find the best way to leave this map(arrive at exit). 
The input of the project can be divided into two parts. The first part is the outside environment input, this means we need to give the project several attributes. This contains, but not limited to the size of the map, 
the layout of the map, the entities in the map, the position of the beasts, the solution of the map and other attributes of the map. 
The second part of the input is the configuration of the agent itself. These inputs will be the HP value of the agent, the speed of the agent, the weapon that the agent will take and other detail attributes of the agent. 
The final output, in the program/code level, will be an action array which contains the actions the agent will take during the whole game process. 
In the game/visual level, the output will be that the agent can successfully finish the map with the lowest cost. 

# 2.3 AI/ML Algorithms

The project will combine the A* search algorithm and alpha-beta pruning algorithm for our agent to generate the actions, 
and we will also build a knowledge-based smart AI to perform the task.

# 2.4 Evaluation Plan

The success of the project means our agent moves out of the map while the agent must be alive during the whole game process, which means the health points(HP) value of the agent should be larger than zero when it get the exit of the map. 
For more advanced improvement, we will enable the agent to find the optimal path in order to arrive at the destination as soon as possible. The optimal path will be chosen by our algorithms with the consideration of the cost of time, 
the cost of health value, and the length of the route as a combination. For metrics, firstly we will manually calculate the best path for our samples. The path will be an int array. Then we will compare the AI solution with the human solution: 
making two linear curves to show accuracy. We also will evaluate the time our agent cost in the map, the health points(HP) our agent has when arrives at the destination, etc. The baseline of the game is using A* Algorithms to generate a 
solution list of actions then push the actions to the agent, or letting the agent take each step immediately calculated by the internals of the algorithm and then using pruning algorithm to remove the bad next steps.

In order to visualize the internals of the algorithm, it is possible for us to draw a two-dimensional map to show all the objects in the map and we can track our agent’s action in a direct way. We would also set different global variables to 
keep track of different attributes of our agents including health points(HP), directions, etc. In order to make sure our agent is “smart”, we will generate several maps with “extreme conditions” for testing, which can also be regarded as 
the “edge cases” of our program. Sanity cases:
	1. Generate a simple map without any dangerous grids and check if our agent can move out the map successfully.
	2. Generate a simple map with some interesting parts and set a solution path. Then manually compare the AI path with our solution to detect something unexpected.
	3. Generate a largely enough map to let the agent starve to death to check if any bugs when the agent failed his mission in the adventure.
	4. Generate a complex map with some dangerous area and food to check whether the AI can using food to extend the agent’s adventure time.

# 2.5 Appointment with the Instructor
The date and time we have reserved the appointment for: 3:15pm - 3:30pm, Wednesday,April 24, 2019