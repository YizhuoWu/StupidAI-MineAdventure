---
layout: default
title: Final Report
---
## 1 Project Video: StupidAI-MineAdventure


## 2 Project Summary

Our project is named MineAdventure. The project is going to be an adventure game for our Minecraft agent. In the project, there will be a randomly generated adventure map 
for our agent, the goal of our agent is to leave this “dangerous” area as soon as possible while our agent is alive, in other words, our agent should use AI/ML algorithms 
to find the best way to leave this map(arrive at destination). We defined the best way as the shortest path from start point to end point while the agent is alive.

## 3 Approaches

In order to find the best way, which is the shortest path while the agent is alive, it is important to find the shortest distance from the current position to the destination, and 
the agent should also avoid the barriers including lavas, iron walls. Hence we chose to use A* search algorithm to decide every step for our agent. A* search algorithm is 
computed by f(n) =g(n) + h(n) where g(n) is the cost we have from the start point to the current position and h(n) is the optimal distance from the current position to the 
destination. Because our agent will have four directions (four possible steps, we did not allow our agent to walk diagonally), so we need to the one which has the smallest 
A* value, which is the f(n) value. We compute g(n) by the formula g(n) = (Full Health Value) - (Health Value Lost Since Start) and we can also compute h(n) by computing distance 
from each nearby points to the destination. Then we can choose the best direction that our agent is going to.

## 4 Evaluation

The success of the project means our agent moves out of the map with the best path while the agent must be alive during the whole game process, which means the health points(HP) 
value of the agent should be larger than zero when it get the exit of the map.

In order to evaluate this, we have different ways to make sure we know and understand the agent’s behavior.

For the shortest path, because we set different variables to keep track of our agent’s position, the start point and destination of the map. So before the agent making the decision, 
our algorithm will compute the best action for our agent to take, and we print them in the console and we let our program sleep for seconds, so we can see every action and computing 
process clearly in order to debug our program easily. At the same time, the most efficient way for us to see if the agent choose the best action is to observe the agent in the 
Minecraft game. If everything goes fine, the agent will walk from the start point to destination with the shortest path and stay alive during the process, and it will avoid any barriers 
including walls or lavas. 

## 5 References
The most important one is the XML schema documentation from the Malmo official. This document is extremely helpful since the tutorial only gives the user a brief look at how 
Malmo works but when one really wants to implement a mission, there are a lot of important attributes or XML features in the document and the explanation is clear.
We also read about alpha-beta pruning algorithm and A* search algorithm from UC Irvine professor Lathrop’s website. The lecture slides explain everything in a very detailed way 
and it helped us a lot when we implement the algorithm and make changes to them.
We also looked through the website https://gitter.im/Microsoft/malmo# to find some useful tips for approaching our functionality (e.g. chat command).