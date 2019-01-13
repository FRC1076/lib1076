import math
def is_in_deadzone(radius, location):
    (x,y) = location
    return(x**2+y**2) <= (radius**2)
    

def deadzone(radius, location):
    if is_in_deadzone(radius, location):
        return(0,0)
    else:
        (x,y) = location
        i = (x**2+y**2)
        r = (math.sqrt(i))
        theta = (math.atan(x/y))
        k =(r-radius)/(1-radius)
        
        t = (x**2/k)
        m = (y**2/k)     
        return(t,m)
    