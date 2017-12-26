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

grid=[  [0, 1, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0], 
        [0, 0, 1, 1, 1, 0], 
        [0, 0, 0, 0, 1, 0]  ]
goal = [len(grid)-1, len(grid[0])-1]
#[len(grid)-1, len(grid[0])-1]
cost = -1
delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

def compute_value(grid,goal,cost):
    ##Initialise states
    end=False
    reached=False
    g_value_grid=[[99 for j in range(len(grid[i]))] for i in range(len(grid))]
    neighbours=[goal]
    
    ##While there is an opprtunity for a path and we haven't reached
    while(not(end)):
        #print(neighbours)
        cost+=1
        next_neighbours=[]
        for neighbour in neighbours:
            x,y=neighbour
            g_value_grid[x][y]=cost
            #print(cost,x,y)
            grid[x][y]=1
            for action in delta:
                i,j=action
                if((x+i>=0) and (y+j>=0) and (x+i<len(grid)) and (y+j<len(grid[i]))):
                    pos=[x+i,y+j]
                    if(grid[x+i][y+j]==0):
                        if(pos not in next_neighbours):
                            next_neighbours.append(pos)
        if(len(next_neighbours)):
            neighbours=next_neighbours
        else: end=True
    
    return (g_value_grid)


def show(a):
    for row in a:
        print(row)
    print("\n")

show(compute_value(grid,goal,cost))
