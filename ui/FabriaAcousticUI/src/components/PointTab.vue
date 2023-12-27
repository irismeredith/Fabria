<script setup>

    import { useModelStoreHex } from '../store.js';

    const props = defineProps(['pointName']);
    
    const geom = useModelStoreHex()

</script>

<template>
    <v-card variant="tonal" id="point-card">
        <v-card-item>
            <v-chip>{{ pointName }}</v-chip>
        </v-card-item>
        <div id="point-tab-container">
            <v-text-field label="x" variant="solo-filled" class="co-ordinate" v-model="geom.model.vertices[pointName][0]"></v-text-field>
            <v-text-field label="y" variant="solo-filled" class="co-ordinate" v-model="geom.model.vertices[pointName][1]"></v-text-field>
            <v-text-field label="z" variant="solo-filled" class="co-ordinate" v-model="geom.model.vertices[pointName][2]"></v-text-field>
        </div>
    </v-card>
</template>

<style>

    .co-ordinate{
        margin: 5px;
    }

    #point-tab-container{
        display: flex;
        flex-direction: row;
        margin: 5px;
    }

    #point-card{
        margin: 10px;
    }

</style>