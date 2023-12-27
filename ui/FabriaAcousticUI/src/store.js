// This file contains two pinia stores: one that contains url data for APIs being called by the frontend app, and one that contains 
// the main application state. Ideally these will later be refactored out into separate files

// Author: Iris Meredith

// Last modified: 27/12/2023

import { defineStore } from 'pinia'


// This is the API store, containing information as to the urls for the backend that this app might call

export const useAPIStore = defineStore('apiStore', {

  state: () => {
    return {

      geometry_api: 'localhost:8080/get-geometry'

    }
  },

})


// This is currently the main application state, though this is subject to change

export const useModelStoreHex = defineStore('modelStoreHex', {

  state: () => {
    return {

      // The state is wrapped in a model object to make it easier to send the whole model block to the backend as a POST request
      // vertices currently stores the vertices of the hexahedron in an anticlockwise loop, with the bottom face coming before the top face
      // facets are faces defined by the vertices: they're associated with acoustic boundary materials
      // blocks define sections of the volume encompassed by the vertices: they're associated with acoustic media
      // compute_parameters defines computational aspects of the model: what solver enginer are we using, and how many points do we want to use?

      model: {

        vertices: {'v_3': [0,1,0], 'v_0': [0,0,0], 'v_7': [0,1,1], 'v_2': [1,1,0], 'v_4': [0,0,1], 'v_1': [1,0,0], 'v_6': [1,1,1], 'v_5': [1,0,1]},

        facets :{'Front': {"verts": ["v_0", "v_1", "v_5", "v_4"], "material": "Perfectly reflective surface"}, 
                'Back': {"verts": ["v_3", "v_2", "v_6", "v_7"], "material": "Perfectly reflective surface"},
                'Left': {"verts": ["v_0", "v_3", "v_7", "v_4"], "material": "Perfectly reflective surface"},
                'Right': {"verts": ["v_1", "v_2", "v_6", "v_5"], "material": "Perfectly reflective surface"},
                'Top': {"verts": ["v_4", "v_5", "v_6", "v_7"], "material": "Perfectly reflective surface"},
                'Bottom': {"verts": ["v_0", "v_1", "v_2", "v_3"], "material": "Perfectly reflective surface"}},
      
        blocks :{'Blocky McBlockface': {"medium": 'Air (room temperature)'}},

        compute_parameters :{'Engine': 'Scikit-FEM Helmholtz solver', 'Sample_points': 1000}

      }
    }
  },

  actions: {
    
    // This action gets geometry data from the server API in VTK format and stores it locally

    async getVTKgeom(){

      const response = await fetch("http://localhost:8080/api/get-geometry", { method: "POST", headers: {"Content-type": "application/json"}, body: JSON.stringify(this.model)})

      // Save the returned file locally in the background

      const vtk_blob = await response.blob()

      sessionStorage.setItem("currentGeom", vtk_blob)

    }

  },

})

