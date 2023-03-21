# Calculate the distance between two points
import math


def dis_of_two_points(p, q):
    return f"The distance between point{p} & point{q} is {math.dist(p, q)}"


print(dis_of_two_points(p=(int(input("Point x1: ")), int(input("Point y1: "))),
                  q=(int(input("Point x2: ")), int(input("Point y2: ")))))
