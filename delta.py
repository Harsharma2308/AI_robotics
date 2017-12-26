# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0]]


init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 0

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right
delta_name=['^','<','v','>']
def search(grid,init,goal,cost):
    ##Initialise states
    end=False
    reached=False
    neighbours=[init]
    pos=init

    #Expand matrix
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    exp_elem_num=0
    
    g_value_grid= [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j]==1):
                g_value_grid[i][j]=-1
    

    if(pos==goal):
        end=True
        reached=True
    
    ##While there is an opprtunity for a path and we haven't reached
    while(not(end)):
        #print(neighbours)
        cost+=1
        next_neighbours=[]
        for neighbour in neighbours:
            x,y=neighbour
            expand[x][y]=exp_elem_num
            exp_elem_num+=1
            grid[x][y]=1
            g_value_grid[x][y]=cost-1
            for action in delta:
                i,j=action
                if((x+i>=0) and (y+j>=0) and (x+i<len(grid)) and (y+j<len(grid[i]))):
                    pos=[x+i,y+j]
                    if(grid[x+i][y+j]==0):
                        if(pos==goal):
                            #print(cost)
                            expand[pos[0]][pos[1]]=exp_elem_num
                            g_value_grid[pos[0]][pos[1]]=cost
                            end=reached=True
                            break
                        elif(pos not in next_neighbours):
                            next_neighbours.append(pos)
            if(end):
                break
        if(len(next_neighbours)):
            neighbours=next_neighbours
            
        else: end=True
    if(end and reached):pass
    else: pass
        
    return g_value_grid,cost

def show(a):
    for row in a:
        print(row)
    print("\n")

def get_shortest_path(g_value_grid,cost,init,goal):
    path_grid=[[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    path_grid[goal[0]][goal[1]]='*'
    pos=goal

    while(cost>0):
        pos,action_idx=check_action(g_value_grid,pos,cost)
        x,y=pos
        path_grid[x][y]=delta_name[(action_idx+2)%len(delta_name)]
        cost-=1
    return path_grid

def check_action(g_value_grid,pos,cost):
    x,y=pos
    #print(pos)
    for idx,action in enumerate(delta):
        i,j=action
        if((x+i>=0) and (y+j>=0) and (x+i<len(grid)) and (y+j<len(grid[i]))):
            pos=[x+i,y+j]
            if(g_value_grid[x+i][y+j]==cost-1):
                return pos,idx
        #print (pos,idx)


show(grid)
g_value_grid,cost=search(grid,init,goal,cost)
show(get_shortest_path(g_value_grid,cost,init,goal))

'''
A Get to know the shortest path  --> B Find which action from one leads to next node
1. Get a matrix with g-values
2. start from goal
3. Previous g-value matrix
'''
