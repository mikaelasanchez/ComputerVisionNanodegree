import math


def sigmoid(x):
    return 1/(1 + math.e ** -x)


point1 = [1, 1]
point2 = [-1, -1]

print("Point 1, x1 + x2: " + str(round(sigmoid(point1[0] + point1[1]), 2)))
print("Point 2, x1 + x2: " + str(round(sigmoid(point2[0] + point2[1]), 2)))
print("Point 1, 10x1 + 10x2: " + str(round(sigmoid(10*point1[0] + 10*point1[1]), 2)))
print("Point 2, 10x1 + 10x2: " + str(round(sigmoid(10*point2[0] + 10*point2[1]), 2)))

print("Therefore, point 2 will give a smaller error")
