#import yi_Adventure_test
import time
import random
def observation_to_nums(obs,base_grid):
    alist = []
    count = 0
    for i in obs:
        value = item_value(i)
        if base_grid[count] == "lava":
            value = -100
        alist.append(value)
        count+=1
    return alist


def item_value(item):
    item = str(item)
    value = 0
    if item == "grass":
        value = 5
    if item == "air":
        value = 5
    if item == "gold_block":
        value = 0
    if item == "iron_block":
        value = 0
    if item == "dirt":
        value = 0
    if item == "redstone_block":
        value = 100
    return value

def find_grass(base_grid):
    count = 0
    alist = []
    for i in base_grid:
        if i == "grass":
            alist.append(count)

        count += 1

    return alist
    

def make_action(index,agent_host,agent_position):

    

    if index == 0:

        agent_host.sendCommand("movenorth 1")
        agent_host.sendCommand("movewest 1")  
        agent_position[1] = agent_position[1] - 1
        agent_position[0] = agent_position[0] + 1
        
    if index == 17:
        agent_host.sendCommand("movesouth 1")
        agent_host.sendCommand('chat /effect @p 17 1 15');
        time.sleep(1)
        

        agent_position[1] = agent_position[1] + 1
    if index == 2:
        agent_host.sendCommand("movenorth 1")
        agent_host.sendCommand("moveeast 1")
        agent_position[1] = agent_position[1] - 1
        agent_position[0] = agent_position[0] + 1
        
    if index == 11:
        agent_host.sendCommand("movewest 1")
        agent_host.sendCommand('chat /effect @p 17 1 15');
        time.sleep(1)
        agent_position[0] = agent_position[0] - 1
    if index == 4:
        print("self")
        pass
    if index == 13:
        agent_host.sendCommand("moveeast 1")
        agent_host.sendCommand('chat /effect @p 17 1 15');
        time.sleep(1)
        agent_position[0] = agent_position[0] + 1     
    if index == 6:
        agent_host.sendCommand("movesouth 1")
        agent_host.sendCommand("movewest 1")
        
        agent_position[1] = agent_position[1] + 1
        agent_position[0] = agent_position[0] - 1
    if index == 7:
        agent_host.sendCommand("movenorth 1")
        agent_host.sendCommand('chat /effect @p 17 1 15');
        time.sleep(1)
        agent_position[1] = agent_position[1] - 1
    if index == 8:
        agent_host.sendCommand("movesouth 1")
        agent_host.sendCommand("moveeast 1")
        agent_position[1] = agent_position[1] + 1
        agent_position[0] = agent_position[0] + 1

def find_best_index(num_list,max_value):
    if num_list[5] == max_value:
        return 5
    if num_list[7] == max_value:
        return 7
    return num_list.index(max_value)


def find_one_step(base_grid,agent_position):
    alist  = [(base_grid[7],7),(base_grid[11],11),(base_grid[13],13),(base_grid[17],17)]
    if agent_position[0] == 0.5:
        alist.remove((base_grid[11],11))
    if agent_position[0] == 58.5:
         alist.remove((base_grid[13],13))
    if agent_position[1] == 58.5:
         alist.remove((base_grid[17],17))
    if agent_position[1] == 0.5:
         alist.remove((base_grid[7],7))
    result = []
    for i in alist:
        if str(i[0]) == "grass" or str(i[0]) == "quartz_block":
            result.append(i[1])
        if str(i[0]) == "redstone_block":
            result = [i[1]]
            return result


    return result

def second_step_list(index,base_grid,agent_position):

    result = []
    if index == 7:
        if agent_position[1] == 1.5:
            result = [6,8]
        else:
            result = [2,6,8]
    if index == 11:
        if agent_position[0] == 1.5:
            result = [6,16]
        else:
            result = [6,10,16]
    if index == 13:
        if agent_position[0] == 57.5:
             result = [8,18]
        else:
            result = [8,14,18]
    if index == 17:
        if agent_position[1] == 57.5:
            result = [16,18]
        else:
            result = [16,18,22]
    return result
        


def compute_second_step(grass_index_list,agent_position,base_grid):

    primary_values = {}

    print("list: " + str(grass_index_list))

    for i in grass_index_list:

        second_steps =  second_step_list(i,base_grid,agent_position)
        print("second_steps: " + str(second_steps))

        values = {}
        

        for p in second_steps:

            if base_grid[p] == "grass" or base_grid[p] == "redstone_block" or base_grid[p] == "quartz_block":

                values[p] = compute_distance(i,p,agent_position)
                #print("ans: " + str(p) + ": " + str(values[p]))
                
                

        sorted_values = sorted(values.items(), key=lambda kv: kv[1])
                
                

        if sorted_values != []:
            
            print("sorted_value: " + str(sorted_values))
            min_val_item = sorted_values[0]
            primary_values[i] = min_val_item[1]



    sorted_values_1 = sorted(primary_values.items(), key=lambda kv: kv[1])
    print("list (index,cost): "+str(sorted_values_1))

    min_val = sorted_values_1[0][1]
    print("min_val: "+str(min_val) )

    flag = 0

    for v in range(1,len(sorted_values_1)):
        if sorted_values_1[v][1] != min_val:
            flag = 1
            index = random.randint(0,v-1)
            break

    if flag == 0:
        index = random.randint(0,len(sorted_values_1)-1)
    #min_index = sorted_values_1[0][0]
    min_index = sorted_values_1[index][0]
    return min_index


def compute_distance(i,p,agent_position):
    print(agent_position)
    distance = (58.5-agent_position[0])+(58.5-agent_position[1])
    if i == 7 or i == 11 :
        dis_temp = distance + 1
        if p == 2 or p == 6 or p == 10:
            return dis_temp + 1
        if p == 16 or p == 8:
            return dis_temp - 1
    elif i == 17 or i == 13:
        dis_temp = distance - 1
        if p == 8 or p == 16:
            return dis_temp + 1
        if p == 14 or p == 18 or p == 22:
            return dis_temp - 1
            
        






# Initial values of Aplha and Beta  
MAX, MIN = 1000, -1000 
  
# Returns optimal value for current player  
#(Initially called for root and maximizer)  
def minimax(depth, nodeIndex, maximizingPlayer,  
            values, alpha, beta):  
   
    # Terminating condition. i.e  
    # leaf node is reached  
    if depth == 3:  
        return values[nodeIndex]  
  
    if maximizingPlayer:  
       
        best = MIN 
  
        # Recur for left and right children  
        for i in range(0, 2):  
              
            val = minimax(depth + 1, nodeIndex * 2 + i,  
                          False, values, alpha, beta)  
            best = max(best, val)  
            alpha = max(alpha, best)  
  
            # Alpha Beta Pruning  
            if beta <= alpha:  
                break 
           
        return best  
       
    else: 
        best = MAX 
  
        # Recur for left and  
        # right children  
        for i in range(0, 2):  
           
            val = minimax(depth + 1, nodeIndex * 2 + i,  
                            True, values, alpha, beta)  
            best = min(best, val)  
            beta = min(beta, best)  
  
            # Alpha Beta Pruning  
            if beta <= alpha:  
                break 
           
        return best  
       
# Driver Code  
#if __name__ == "__main__":  
   
    #values = [3, 5, 6, 9, 1, 2, 0, -1]   
    #print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))  
      
