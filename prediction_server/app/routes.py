from app import app
from pprint import pprint
import json
from flask import request, send_from_directory
from sys import stderr
from training_data import generate_random_hex, generate_hex_mesh

# This route takes a set of vertex points in scikit-fem's canonical order and returns a .vtk file containing
# the geometry


@app.route('/api/get-geometry', methods=['GET', 'POST'])
def get_geometry():

    verts = list(request.get_json()["vertices"].values())

    mesh = generate_hex_mesh(verts)

    mesh.save('/home/iris/PycharmProjects/Fabria/prediction_server/app/tmp/tmp.vtk')

    # return send_from_directory(directory='/home/iris/PycharmProjects/Fabria/prediction_server/app/tmp', path='tmp.vtk',
    #                           as_attachment=False)

    return send_from_directory(directory='/home/iris/PycharmProjects/Fabria/prediction_server/app/tmp/teapot',
                               path='scene.gltf', as_attachment=False)
