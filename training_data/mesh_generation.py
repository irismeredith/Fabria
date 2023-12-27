import random
import math
import numpy as np
from skfem import *


# This function generates a random convex hexahedron that scikit-fem can then generate a mesh from

def generate_random_hex(size, skew):

    x = random.randint(1, size)

    y = random.randint(1, size)

    z = random.randint(1, size)

    skew_x = math.ceil(x * skew)

    skew_y = math.ceil(y * skew)

    skew_z = math.ceil(z * skew)

    vert_0 = [0, 0, 0]

    vert_6 = [x, y, z]

    vert_1 = [0, vert_6[1] + random.randint(-skew_y, skew_y), 0]

    vert_2 = [vert_6[0] + random.randint(-skew_x, skew_x), vert_6[1] + random.randint(-skew_y, skew_y), 0]

    vert_3 = [vert_6[0] + random.randint(-skew_x, skew_x), 0, 0]

    vert_4 = [0, 0, vert_6[2] + random.randint(-skew_z, skew_z)]

    vert_5 = [0, vert_6[1] + random.randint(-skew_y, skew_y), vert_6[2] + random.randint(-skew_z, skew_z)]

    vert_7 = [vert_6[0] + random.randint(-skew_x, skew_x), 0, vert_6[2] + random.randint(-skew_z, skew_z)]

    return np.array([vert_3, vert_0, vert_7, vert_2, vert_4, vert_1, vert_6, vert_5]).T


def generate_hex_mesh(verts):

    mesh = MeshHex(np.array(verts).T, np.array([[0, 1, 2, 3, 4, 5, 6, 7]]).T)

    return mesh
