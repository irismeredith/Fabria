// This store contains information about the various computational engines available to us: right now that's just the scikit-FEM solver that
// I'm using to generate training data, but who knows where things will go?

// Author: Iris Meredith

// Last modified: 27/12/2023

import { defineStore } from 'pinia'


export const useEngineStore = defineStore('engineStore', {

  state: () => {
    return {

        engines: ['Scikit-FEM Helmholtz solver']

    }
  },

})
