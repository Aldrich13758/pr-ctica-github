import math 
x=float(input()) 
floor=math.floor(x)
ceil=math.ceil(x) 
round=int(ceil 
              if x - floor == 0.5 
              else round(x))
print(floor, ceil, round)