<script setup lang="ts">
import ElementWrapper from './ElementWrapper.vue'
import TheForm from './TheForm.vue'
import TheQR from './TheQR.vue'
import TheMandate from './TheMandate.vue'
import TheSuccess from './TheSuccess.vue'
import { ref } from 'vue'

const contentNr = defineModel({ type: Number, required: true })
const refnr = ref('')
const sum = ref(0.0)
const name = ref('')
const iban = ref('')
</script>

<template>
  <ElementWrapper class="main-wrapper my-1.5 place-content-center content-center">
    <TheForm
      v-model:refnr="refnr"
      v-model:sum="sum"
      v-model:contentNr="contentNr"
      v-if="contentNr === 1"
    />
    <TheQR
      v-else-if="contentNr === 2"
      v-model:name="name"
      v-model:iban="iban"
      v-model:contentNr="contentNr"
    />
    <TheMandate
      v-else-if="contentNr === 3"
      v-model:name="name"
      v-model:iban="iban"
      v-model:contentNr="contentNr"
    />
    <TheSuccess v-else-if="contentNr === 4" />
  </ElementWrapper>
</template>

<style scoped>
.main-wrapper {
  height: 50vh;
}
</style>
