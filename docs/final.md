---
layout: default
title: Final Report
---
## 1 Project Video: StupidAI-MineAdventure
<iframe width="560" height="315" src="https://www.youtube.com/embed/xDyvuzzZx9k" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## 2 Project Summary

Our project is named MineAdventure. The project is going to be an adventure game for our Minecraft agent. In the project, there will be a randomly generated adventure map 
for our agent, the goal of our agent is to leave this “dangerous” area as soon as possible while our agent is alive, in other words, our agent should use AI/ML algorithms 
to find the path to leave this map(arrive at destination). The destination is the red block on the map and we also put the statement “mission stopped” to indicate that we 
arrived at the destination.

## 3 Approaches

In order to find the path to success while the agent is alive, it is important to for our agnet to avoid the barriers including lavas,lakes, forests and iron walls. Hence we 
chose to use A* search algorithm to decide every step for our agent. 
A* search algorithm is computed by f(n) = g(n) + h(n). We define ‘g(n)’ and ‘h(n)’ as simply as possible below
	
	g(n) = abs(startpoint.x - currentpoint.x) + abs (startpoint.y - currentpoint.y)
	(actual cost from start point to current point by using Manhattan distance)
	
and we explored different heuristics:

	(1) h(n) = abs(currentpoint.x - destination.x) + abs (currentpoint.y - destination.y)
		(actual cost from current point to destination point by using Manhattan distance)
		Since we have same distance among all points and g(n) + h(n) in this situation will produce same value for every points, we decided to ignore g(n)
		and changed the formula to f(n) = h(n). It is also named Best-First search. 
	
	(2) h(n) = math.sqrt ((currentpoint.x - destination.x) ** 2 + (currentpoint.y - destination.y)**2)
		(optimal cost from current point to destination by using Euclidean distance)

Because our agent will have four directions (four possible steps, we did not allow our agent to walk diagonally), so at each step we need to choose the point with has the lowest
A* value, which is the f(n) value. Then our agnet will move to the direciton with that point. 

## 4 Evaluation

The success of the project means our agent moves out of the map(arrive at the destination) while the agent must be alive during the whole game process, which means the health points
(HP) of the agent should be larger than zero when it gets the exit of the map. The agent with fewer total steps will be treat as more effective.
For example, the following screenshots show the situation of success and failure
 
Success (The agent successfully arrived at the destination with health points(HP) > 0)

![alt text](https://github.com/YizhuoWu/StupidAI-MineAdventure/blob/master/docs/arts/Evaluation/complexA.png?raw=true"complexA")

Failure (The agent was died on the way to escape the map because of starvation)

![alt text](https://github.com/YizhuoWu/StupidAI-MineAdventure/blob/master/docs/arts/Evaluation/complexB.png?raw=true"complexB")

In order to evaluate this, we have different ways to make sure we know and understand the agent’s behavior.
For the first heuristic(f(n) = h(n)), because we set different variables to keep track of our agent’s position, the start point and destination of the map. So before the agent making 
the decision, our algorithm will compute the best action for our agent to take, and we print them in the console and we let our program sleep for seconds, so we can see every action 
and computing process clearly in order to debug our program easily. At the same time, the most efficient way for us to see if the agent chooses the best action is to observe the agent 
in the Minecraft game. If everything goes fine, the agent will walk from the start point to destination with the shortest path and stay alive during the process, and it will avoid any
barriers including walls or lavas. 
As we can see in the following screenshot that the agent successfully arrived at the destination(red block) with health points > 0 and the total steps the agent spent is shown on the 
console.(total steps: 117)
 
![alt text](https://github.com/YizhuoWu/StupidAI-MineAdventure/blob/master/docs/arts/Evaluation/normalB.png?raw=true"normalB")


For the second heuristic(f(n) = g(n) + h(n)), because the algorithm will calculate the best path to destination firstly and print the positions of the path to the console, we can see 
the coordinates of every steps and computing process clearly in order to debug our program easily. At the same time, the most efficient way for us to see if the agent chooses the best 
action is to observe the agent in the Minecraft game. If everything goes fine, the agent will walk from the start point to destination with the shortest path and stay alive during the
process, and it will avoid any barriers including walls or lavas.
As we can see in the following screenshot that the agent successfully arrived at the destination(red block) with health points > 0 and the total steps the agent spent is shown on the 
console.(total steps: 116)

![alt text](https://github.com/YizhuoWu/StupidAI-MineAdventure/blob/master/docs/arts/Evaluation/normalA.png?raw=true"normalA")


To sum up, since we run the two algorithms on the same map(as shown above), we can conclude that the second heuristic is more effective than the first one because of the fewer 
total steps.
## 5 References
The most important one is the XML schema documentation from the Malmo official. This document is extremely helpful since the tutorial only gives the user a brief look at how 
Malmo works but when one really wants to implement a mission, there are a lot of important attributes or XML features in the document and the explanation is clear.
We also read about alpha-beta pruning algorithm and A* search algorithm from UC Irvine professor Lathrop’s website. The lecture slides explain everything in a very detailed way 
and it helped us a lot when we implement the algorithm and make changes to them.
We also looked through the website https://gitter.im/Microsoft/malmo# to find some useful tips for approaching our functionality (e.g. chat command).