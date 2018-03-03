# -----------
# User Instructions
#
# Define a function smooth that takes a path as its input
# (with optional parameters for weight_data, weight_smooth,
# and tolerance) and returns a smooth path. The first and 
# last points should remain unchanged.
#
# Smoothing should be implemented by iteratively updating
# each entry in newpath until some desired level of accuracy
# is reached. The update should be done according to the
# gradient descent equations given in the instructor's note
# below (the equations given in the video are not quite 
# correct).
# -----------

from copy import deepcopy

# thank you to EnTerr for posting this on our discussion forum
def printpaths(path,newpath):
    for old,new in zip(path,newpath):
        print ('['+ ', '.join('%.3f'%x for x in old) + \
               '] -> ['+ ', '.join('%.3f'%x for x in new) +']')

# Don't modify path inside your function.
path = [[0, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [2, 2],
        [3, 2],
        [4, 2],
        [4, 3],
        [4, 4]]

def smooth(path, weight_data = 0.5, weight_smooth = 0.1, tolerance = 0.000001):
    # Make a deep copy of path into newpath
    newpath = deepcopy(path)
    
    check_stop = False
    while (not check_stop):
        oldpath= deepcopy(newpath)
        check_stop=True
        ##Smoothing
        for idx, entry in enumerate(newpath):
            if(idx ==0 or idx==len(path)-1): continue
            for j,entry2 in enumerate(newpath[idx]):
                newpath[idx][j]+= weight_smooth*(newpath[idx+1][j]+newpath[idx-1][j]-2*newpath[idx][j]) + weight_data*(path[idx][j]-newpath[idx][j])
                
                if(check_stop):
                    dif=abs(oldpath[idx][j]-newpath[idx][j])
                    print(dif)
                    check_stop=dif<tolerance
  
    return newpath
printpaths(path,smooth(path))
