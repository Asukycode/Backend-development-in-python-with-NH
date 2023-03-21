# Calculate the distance between two points
import math

entry_p = (int(input("Point x1: ")), int(input("Point y1: ")))
entry_q = (int(input("Point x2: ")), int(input("Point y2: ")))


print(f"The distance between point{entry_p} & point{entry_q} is {math.dist(entry_p,entry_q)}")