# Helmholtz formulation it is, then. I should be able to reconstruct a time-dependent solution using separation of
# variables

# Alright, next step is to actually get solutions out of this: that might be a job for tomorrow. But once that's done,
# I have a pipeline for training and validation data generation mostly ready

import numpy as np
from training_data import generate_random_hex
from scipy.sparse import identity
from skfem import *
from skfem.models import laplace, mass

# Generate a random hexahedral mesh

corners = generate_random_hex(10, 0)

print(corners)


# Label boundaries

def get_boundary(vect, verts, b_name):

    boundaries = {'front': {verts[0][0], verts[0][1], verts[0][5], verts[0][4]},
                  'back': {verts[0][3], verts[0][2], verts[0][6], verts[0][7]},
                  'left': {verts[1][0], verts[1][3], verts[1][7], verts[1][4]},
                  'right': {verts[1][1], verts[1][2], verts[1][6], verts[1][5]},
                  'top': {verts[2][4], verts[2][5], verts[2][6], verts[2][7]},
                  'bottom': {verts[2][0], verts[2][1], verts[2][2], verts[2][3]}}

    return np.isin(vect, boundaries[b_name])


m = MeshHex(corners, np.array([[0, 1, 2, 3, 4, 5, 6, 7]]).T).refined(2)

print(m.doflocs)
print(m.t)

# Create the basis associated with the mesh

e = ElementHex2()
ib = Basis(m, e)

# Assemble matrices

A = laplace.assemble(ib)
M = mass.assemble(ib)

# Apply boundary conditions


dofs = ib.get_dofs('left')

L, x = solve(*condense(A, M, D=dofs), solver=solver_eigen_scipy_sym(k=10))

# Solve the resultant system for the Helmholtz equation: find eigenvalues and eigenvectors

if __name__ == "__main__":
    from os.path import splitext
    from sys import argv

    m.save(splitext(argv[0])[0] + '.vtk')
