<script setup>

    import BlockTab  from '../components/BlockTab.vue';

</script>

<template>
    <v-sheet color="deep-purple-darken-3" id="vert-sheet">
        <BlockTab blockName="Blocky McBlockface" />
    </v-sheet>
</template>

<style>

    #vert-sheet{
        align-self: stretch;
        justify-self: stretch;
        padding: 10px;
    }

</style>