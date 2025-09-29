x, y = map(float, input().split())
r1 = 3
r2 = 5
t = x + y 
if (t >= r1) and (t <= r2) and (x >= 0):
    print(True)
else:
    print(False)