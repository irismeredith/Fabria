// A pinia store containing details of surface materials and propagation media to be displayed on the front-end

//Author: Iris Meredith

//Last modified: 27/12/2023

import { defineStore } from 'pinia'


export const useMaterialStore = defineStore('materialStore', {

  state: () => {

    // Materials are surface materials: media are bulk materials

    return {

      materials : ['Perfectly absorbent surface', 'Perfectly reflective surface', 'Add material...'],
      media : ['Air (room temperature)', 'Argon', 'Water']

    }
  },

})
