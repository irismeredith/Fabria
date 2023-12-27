
<script setup>

    import { useModelStoreHex } from '../store.js';
    import { useMaterialStore } from '../material_store.js';

    const props = defineProps(['blockName']);

    const materials = useMaterialStore()
    const model = useModelStoreHex()

</script>

<template>
    <v-card variant="tonal" id="point-card">
        <v-card-item>
            <v-chip>{{ blockName }}</v-chip>
        </v-card-item>
        <div id="point-tab-container">
            <v-select label="Select block medium" :items=materials.media v-model="model.model.blocks[blockName].medium"></v-select>
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