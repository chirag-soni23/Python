# 4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.
import math

def circle_stats(radius):
     area =  math.floor(math.pi * radius ** 2)
     circumference = math.floor(2 * math.pi * radius)
     return area, circumference

a, c = circle_stats(2)
print("Area :", a, "Circumference: ", c)

