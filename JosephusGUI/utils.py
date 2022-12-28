import numpy as np
from JosephusGUI.constants import CIRCLE_CENTER, RADIUS, SCREEN_SIZE


# calculates the coordination on a circle
def coordinations(num, radius=RADIUS):
    angles = np.linspace(0, 2*np.pi, num+1)
    coordinates = []
    radius += num
    if radius > (SCREEN_SIZE[0]//2 - 20):
        radius = SCREEN_SIZE[0]//2 - 20
    for ang in angles:
        x = CIRCLE_CENTER[0] + radius*np.cos(ang)
        y = CIRCLE_CENTER[1] + radius*np.sin(ang)
        coordinates.append((x, y))
    # returning coordinates as tuples
    return coordinates


# gives us the answer to the josephus problem
def josephus_solver(num):
    reduced = bin(num)[3:]
    reduced += '1'
    return int(reduced, 2)
