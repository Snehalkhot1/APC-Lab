import math

points = [(2,3), (5,6), (8,1), (4,9)]

def distance(p1, p2):
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

print("Points:", points)

p1 = points[0]
p2 = points[1]

print("Distance between", p1, "and", p2, "=", distance(p1,p2))

origin = (0,0)
farthest = points[0]
max_dist = distance(origin, farthest)

for p in points:
    d = distance(origin, p)
    if d > max_dist:
        max_dist = d
        farthest = p

print("Farthest Point from Origin:", farthest)