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


init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
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

    #Expand matrix
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    
    exp_elem_num=0


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
            for action in delta:
                i,j=action
                if((x+i>=0) and (y+j>=0) and (x+i<len(grid)) and (y+j<len(grid[i]))):
                    pos=[x+i,y+j]
                    if(grid[x+i][y+j]==0):
                        if(pos==goal):
                            #print(cost)
                            expand[pos[0]][pos[1]]=exp_elem_num
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
        
    return expand

def show(a):
    for row in a:
        print(""*1+"{0}".format(row))
    print("\n")
show(grid)
show(search(grid,init,goal,cost))


