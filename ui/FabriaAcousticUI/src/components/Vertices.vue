<script setup>

    import PointTab  from '../components/PointTab.vue';

</script>

<template>
    <v-sheet color="deep-purple-darken-3" id="vert-sheet">
            <PointTab pointName="v_0" />
            <PointTab pointName="v_1" />
            <PointTab pointName="v_2" />
            <PointTab pointName="v_3" />
            <PointTab pointName="v_4" />
            <PointTab pointName="v_5" />
            <PointTab pointName="v_6" />
            <PointTab pointName="v_7" />
    </v-sheet>
</template>

<style>

    #vert-sheet{
        align-self: stretch;
        justify-self: stretch;
        padding: 10px;
    }

</style>