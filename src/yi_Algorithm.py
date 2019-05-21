def observation_to_nums(obs):
    alist = []
    for i in obs:
        value = item_value(i)
        alist.append(value)
    return alist


def item_value(item):
    item = str(item)
    value = 0
    if item == "grass":
        value = 5
    if item == "dirt":
        value = 0
    if item == "redstone_block":
        value = 100
    return value

def make_action(index,agent_host):
    if index == 0:
        agent_host.sendCommand("move -1")
        agent_host.sendCommand("strafe +1")        
    if index == 1:
        agent_host.sendCommand("move -1")
    if index == 2:
        agent_host.sendCommand("move -1")
        agent_host.sendCommand("strafe -1")        
    if index == 3:
        agent_host.sendCommand("strafe +1")
    if index == 4:
        print("self")
        pass
    if index == 5:
        agent_host.sendCommand("strafe -1")
    if index == 6:
        agent_host.sendCommand("move 1")
        agent_host.sendCommand("strafe +1")
    if index == 7:
        agent_host.sendCommand("move 1")
    if index == 8:
        agent_host.sendCommand("move 1")
        agent_host.sendCommand("strafe -1")

def find_best_index(num_list,max_value):
    if num_list[7] == max_value:
        return 7
    if num_list[5] == max_value:
        return 5
    return num_list.index(max_value)
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
      
