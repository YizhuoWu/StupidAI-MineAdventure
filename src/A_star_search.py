import math
import random
import time
class Block:
    def __init__(self,index,position,grid):
        self.position = position
        self.index = index
        self.parent = None
        self.h = 0
        self.g = 0
        self.type = grid



def Manhattan_distance(pos1,pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def Euclidean_distance(pos1,pos2):
    return math.sqrt ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1])**2)






def astar_search(full_grid):
    info_dict = {}
    info_dict[0] = Block(0,[0,0],"quartz_block")
    info_dict[0].h = Euclidean_distance(info_dict[0].position,[58,58])
    info_dict[3480] = Block(3480,[58,58],"redstone_block")
    

    positions = []
    for i in range(59):
        for j in range(59):
            positions.append([j,i])
    #return positions
    
    route_list = [(i,v) for i, v in enumerate(full_grid) if v == "grass"]
    for b in route_list:
        index = b[0]
        grid = b[1]
        position = positions[index]
        info_dict[index] = Block(index,position,grid)

    openlist = []
    closelist = []

    current = info_dict[0]

    openlist.append(current)
    while (len(openlist) != 0):

        print("open length: "+ str(len(openlist)))
        print("close length: "+ str(len(closelist)))
        if len(openlist) > 1:
            sorted_openlist = sorted(openlist, key=lambda block: block.h + block.g)
        
            min_val = sorted_openlist[0].h + sorted_openlist[0].g
            print("min_val: " + str(min_val))
            flag = 0
        
            for v in range(1,len(sorted_openlist)):
                #print("v: " + str(v))
                if sorted_openlist[v].h+sorted_openlist[v].g != min_val:
                #print("v1: " + str(v))
                    flag = 1
                    ind = random.randint(0,v-1)
                    break
        
            if flag == 0:
                ind = random.randint(0,len(sorted_openlist)-1)
            
            q = sorted_openlist[ind]
        else:
            q = openlist[0]

        if q.position == info_dict[3480].position:
            print("end\n")
            path = []
            while (q.parent != None):
                path.append(q)
                q = q.parent
            path.append(q)
            return path[::-1]

        #print(q.position)

        
        openlist.remove(q)
        closelist.append(q)
        for key in info_dict.keys():
            
            if (abs(q.position[0]-info_dict[key].position[0]) == 1  and q.position[1] == info_dict[key].position[1])or (abs(q.position[1]-info_dict[key].position[1]) == 1 and q.position[0] == info_dict[key].position[0]):

                
                if info_dict[key] in closelist:
                    continue
                if info_dict[key] in openlist:
                    new_g = q.g + 1
                    if info_dict[key].g > new_g:
                        info_dict[key].g = new_g
                        info_dict[key].parent = q
                else:
                    info_dict[key].g = q.g + 1
                    info_dict[key].h = Euclidean_distance(info_dict[key].position,[58,58])
                    info_dict[key].parent = q
                    openlist.append(info_dict[key])

def get_actions(route):
    lst = []
    for i in range(len(route)-1):
        curr_block,next_block = route[i:(i+2)]
        if curr_block.position[0] == next_block.position[0]:
            if next_block.position[1] - curr_block.position[1] == 1:
                lst.append("movesouth 1")
            else:
                lst.append("movenorth 1")
        else:
            if next_block.position[0] - curr_block.position[0] == 1:
                lst.append("moveeast 1")
            else:
                lst.append("movewest 1")
    return lst
    
              
                    
                    
        



        
                
