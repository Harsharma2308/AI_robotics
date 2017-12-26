forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']
#orientation=0,1,2,3 => u,r,d,l

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]
goal = [len(grid)-1, len(grid[0])-1]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost_step = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]



def optimum_policy2D(grid,init,goal,cost):

    ##Initialise states
    end=False
    reached=False
    value_grid=[999]

    g_val_grid=[[[999 for item in entry] for entry in grid], [[999 for item in entry] for entry in grid],[[999 for item in entry] for entry in grid],[[999 for item in entry] for entry in grid]]
    policy=[[[' ' for item in entry] for entry in grid], [[999 for item in entry] for entry in grid],[[999 for item in entry] for entry in grid],[[999 for item in entry] for entry in grid]]
    policy2D=[[[' ' for item in entry] for entry in grid]

    ####SETUP#####
    neighbours=[goal]
    for orientation in range(4):
        g_val_grid[orientation][goal[0]][goal[1]]=0
        policy[orientation][goal[0]][goal[1]]='*'

    ##While there is an opportunity for a path and we haven't reached
    while(not(end)):
        #print(neighbours)
        next_neighbours=[]
        for neighbour in neighbours:
            x,y=neighbour
            for idx,action in enumerate(delta):
                i,j=action
                if((x+i>=0) and (y+j>=0) and (x+i<len(grid)) and (y+j<len(grid[i]))) and (grid[x+i][y+j]==0):
                    pos=[x+i,y+j]
                    set_gvalue(neighbour,pos,idx)
                    policy[pos[0]][pos[1]]=delta_name[(idx+2)%4]
                    next_neighbours.append(pos)
        if(len(next_neighbours)):
            neighbours=next_neighbours
        else: end=True
    return policy2D

def set_gvalue(neighbour,pos,idx):
    reverse_index=(idx+2)%4

    val=g_value_grid[reverse_index][neighbour[0]][neighbour[1]]+1+cost_step[1] ##Straight
    if(g_value_grid[reverse_index][pos[0]][pos[1]]>val):g_value_grid[reverse_index][pos[0]][pos[1]]=val
    else : val=g_value_grid[reverse_index][pos[0]][pos[1]]

    policy[reverse_index][pos[0]][pos[1]]=action_name

    left_val=val+cost_step[2] ##Left turn
    if(g_value_grid[reverse_index+1][pos[0]][pos[1]]>left_val):g_value_grid[reverse_index+1][pos[0]][pos[1]]=left_val

    right_val=val+cost_step[0] ##Right turn
    if(g_value_grid[reverse_index-1][pos[0]][pos[1]]>right_val):g_value_grid[reverse_index-1][pos[0]][pos[1]]=right_val    

def show(a):
    for row in a:
        print(row)
    print("\n")

show(optimum_policy2D(grid,init,goal,cost))
