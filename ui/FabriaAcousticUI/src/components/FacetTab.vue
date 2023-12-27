// This component represents a tab containing facets 

<script setup>

    import { useModelStoreHex } from '../store.js';
    import { useMaterialStore } from '../material_store.js';

    const props = defineProps(['facetID'])

    const materials = useMaterialStore()
    const model = useModelStoreHex()

</script>

<template>
    <v-card variant="tonal" id="facet-card">
        <v-card-item>
            <v-chip>{{ facetID }}</v-chip>
        </v-card-item>
        <v-card-item>
            <v-chip>{{ model.model.facets[facetID].verts[0] }}</v-chip>
            <v-chip>{{ model.model.facets[facetID].verts[1] }}</v-chip>
            <v-chip>{{ model.model.facets[facetID].verts[2] }}</v-chip>
            <v-chip>{{ model.model.facets[facetID].verts[3] }}</v-chip>
        </v-card-item>
        <div id="material-selection">
            <v-select label="Select facet material" :items=materials.materials v-model="model.model.facets[facetID].material" id="material"></v-select>
        </div>
    </v-card>
</template>

<style>

    #material{
        margin-left: 10px;
        margin-right: 10px;
    }

    #facet-card{
        margin: 10px;
    }

</style>