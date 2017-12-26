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
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]


grid=[  [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0] ]

init = [2, 5]
goal = [4,3]#[len(grid)-1, len(grid[0])-1]
cost = 0

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

def search(grid,init,goal,cost):
    ##Initialise states
    end=False
    reached=False
    neighbours=[init]
    pos=init
    if(pos==goal):
        end=True
        reached=True
    
    ##While there is an opprtunity for a path and we haven't reached
    while(not(end)):
        print(neighbours)
        cost+=1
        next_neighbours=[]
        for neighbour in neighbours:
            
            x,y=neighbour
            grid[x][y]=1
            for action in delta:
                i,j=action
                if((x+i>=0) and (y+j>=0) and (x+i<len(grid)) and (y+j<len(grid[i]))):
                    pos=[x+i,y+j]
                    if(grid[x+i][y+j]==0):
                        if(pos==goal):
                            print(cost)
                            end=reached=True
                            break
                        elif(pos not in next_neighbours):
                            next_neighbours.append(pos)
            if(end):
                break
        if(len(next_neighbours)):
            neighbours=next_neighbours
            
        else: end=True
    if(end and reached):return([cost,pos[0],pos[1]])
    else: return("Fail")
        
    #return path
print (search(grid,init,goal,cost))
