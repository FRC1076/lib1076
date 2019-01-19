import math
def is_in_deadzone(radius, location):
    (x,y) = location
    return(x**2+y**2) <= (radius**2)
    

def deadzone(radius, location):
    (x,y) = location
    if is_in_deadzone(radius, location):
        return(0,0)
    elif location[0] == 0:
        ny = ((y-radius)/(1 - radius))
        return(0,ny)
        # convert on axis

        
    else:
        i = (x**2+y**2)
        r = (math.sqrt(i))
        theta = (math.atan(x/y))
        k =(r-radius)/(1-radius)
        nx = (r*math.cos(theta)) 
        newy = (r*math.sin(theta))
        return(nx,newy)
    