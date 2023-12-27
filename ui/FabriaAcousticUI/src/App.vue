// This is the root app component for the acoustis modelling app as it currently stands

<script setup>
  import RenderWindow from './components/RenderWindow.vue';
  import Vertices from './components/Vertices.vue';
  import Facets from './components/Facets.vue';
  import Blocks from './components/Blocks.vue';
  import Engine from './components/Engine.vue';

  import { useModelStoreHex } from './store.js';

  const store = useModelStoreHex()

  // Fetch initial geometry data from the store

  store.getVTKgeom()

</script>

<template>
  <div id="app-container">
    <div id="left-bar">
      <v-expansion-panels variant="accordion" multiple color="deep-purple-darken-4">

        <v-expansion-panel title="Vertices" color="deep-purple-darken-4">
          <v-expansion-panel-text  class="expansion-panel-full">
            <Vertices />
          </v-expansion-panel-text>
        </v-expansion-panel>

        <v-expansion-panel title="Facets" color="deep-purple-darken-4">
          <v-expansion-panel-text class="expansion-panel-full">
            <Facets />
          </v-expansion-panel-text>
        </v-expansion-panel>

        <v-expansion-panel title="Blocks" color="deep-purple-darken-4">
          <v-expansion-panel-text  class="expansion-panel-full">
            <Blocks />
          </v-expansion-panel-text>
        </v-expansion-panel>

        <v-expansion-panel title="Computational parameters" color="deep-purple-darken-4">
          <v-expansion-panel-text class="expansion-panel-full">
            <Engine />
          </v-expansion-panel-text>
        </v-expansion-panel>

      </v-expansion-panels>
    </div>

    <div id="three-display">
      <RenderWindow />
    </div>

    <div id="right-bar">

    </div>

  </div>
</template>

<style scoped>

  #app-container{

    display: grid;
    grid-template-rows: 100vh;
    grid-template-columns: 20vw 80vw;

  }

  #left-bar{

    grid-row: 1;
    grid-column: 1;

    background-color: #271675;

    overflow-y: scroll;
  }

  #three-display{

    grid-row: 1;
    grid-column: 2;

  }

  .expansion-panel-full :deep(.v-expansion-panel-text__wrap){
    margin: 0;
    padding: 0;
  }

</style>