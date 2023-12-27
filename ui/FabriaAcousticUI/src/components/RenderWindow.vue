// This component is the 3D rendering window that shows the geometry being modelled. It uses TresJS and 

<script setup>
  import { TresCanvas } from '@tresjs/core'
  import { OrbitControls } from '@tresjs/cientos'
  import { useLoader } from '@tresjs/core'
  import { GLTFLoader } from 'three/addons/loaders/GLTFLoader'
  import { onMounted } from 'vue';


  // This does not appear to currently be working: the blob exists in local storage, but getting it out of storage and into a form that Tres
  // recognises is a definite challenge

  onMounted(() => {

    var current_geom_file = URL.createObjectURL(new File([sessionStorage.getItem("currentGeom")], "tmp.gltf"))

    const { D_model } = useLoader(VTKLoader, current_geom_file)
  
  })

</script>

<template>
  <Suspense>
    <TresCanvas preset="realistic">
      <TresPerspectiveCamera :args="[45, 1, 0.1, 1000]"/>
      <primitive :object="D_model" />
      <TresAmbientLight :intensity="2" />
      <TresDirectionalLight />
      <OrbitControls />
    </TresCanvas>
  </Suspense>
</template>

<style scoped>

</style>