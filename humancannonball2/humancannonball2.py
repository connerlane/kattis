from math import cos, sin, radians, pow

cases = int(input())
for i in range(cases):
    intial_velocity, theta, x1, h1, h2 = [float(e) for e in input().split()]
    x_comp = cos(radians(theta)) * intial_velocity
    y_comp = sin(radians(theta)) * intial_velocity
    time = x1 / x_comp
    acceptable_upper_limit = h2 - 1
    acceptable_lower_limit = h1 + 1
    height = (y_comp * time) - (0.5*9.81*(pow(time, 2)))
    if acceptable_lower_limit < height < acceptable_upper_limit:
        print("Safe")
    else:
        print("Not Safe")

