import numpy as np


def calculateGradient(cuboid):
    volG = abs(cuboid[..., :-1] - cuboid[..., 1:])

    return np.sum(volG)
