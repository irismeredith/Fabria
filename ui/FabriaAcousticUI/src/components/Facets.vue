<script setup>

    import FacetTab  from '../components/FacetTab.vue';

</script>

<template>
    <v-sheet color="deep-purple-darken-3" id="vert-sheet">
        <FacetTab facetID="Front" />
        <FacetTab facetID="Back" />
        <FacetTab facetID="Left" />
        <FacetTab facetID="Right" />
        <FacetTab facetID="Top" />
        <FacetTab facetID="Bottom" />
    </v-sheet>
</template>

<style>

    #vert-sheet{
        align-self: stretch;
        justify-self: stretch;

    }

</style>