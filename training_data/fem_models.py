from skfem import *
from skfem.helpers import dot, grad


# Should I write this as an abstract class and have other things inherit from it? Maybe later

class AcousticModel:
    # Points is a 3D numpy array containing the spatial co-ordinates of our sample points
    def __init__(self, points):

        self.points = points
        self.mesh = None

    def create_mesh(self, element_type):

        if element_type == 'Hex1':

            pass

        elif element_type == 'Hex2':

            pass

        else:

            print('The current element type is not yet supported. Watch this space...')