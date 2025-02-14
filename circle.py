
from random import random
def get_point_on_circle():
    x=abs(random()*2-1.0)
    y=abs(random()*2-1.0)
    if x*x+y*y<1:
        return f"({x},{y})"
print(get_point_on_circle())