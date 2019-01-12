

def is_in_deadzone(radius, location):
    (x,y) = location
    return(x**2+y**2) < (radius**2)