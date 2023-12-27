<script setup>

import { useEngineStore } from '../engine_store.js'
import { useModelStoreHex } from '../store.js';

const engine = useEngineStore()
const model = useModelStoreHex()

</script>

<template>
    <v-sheet color="deep-purple-darken-3" id="vert-sheet">
        <v-select label="Computational engine" :items="engine.engines" v-model="model.model.compute_parameters.Engine"></v-select>
        <v-text-field label="Sample points" v-model="model.model.compute_parameters.Sample_points"></v-text-field>
    </v-sheet>
</template>

<style>

    #vert-sheet{
        align-self: stretch;
        justify-self: stretch;
        padding: 10px;
    }

</style>