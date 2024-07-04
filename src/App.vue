<script setup lang="ts">
import { ref } from 'vue'
import TheHeader from './components/TheHeader.vue'
import TheNavigator from './components/TheNavigator.vue'
import MainContent from './components/MainContent.vue'

const contentNr = ref(1)
</script>

<template>
  <div class="h-screen">
    <header>
      <TheHeader />
    </header>

    <main>
      <MainContent v-model="contentNr" />
      <TheNavigator v-model="contentNr" />
    </main>
  </div>
</template>

<style scoped></style>
