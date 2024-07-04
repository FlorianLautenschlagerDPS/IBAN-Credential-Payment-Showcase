<script setup lang="ts">
import ElementWrapper from './ElementWrapper.vue'
import AppButtonCircled from './buttons/AppButtonCircled.vue'
import ArrowRightIcon from 'vue-material-design-icons/ArrowRight.vue'
import ArrowLeftIcon from 'vue-material-design-icons/ArrowLeft.vue'
import { computed } from 'vue'

const contentNr = defineModel({ type: Number, default: 1 })

const isHighest = computed(() => {
  return contentNr.value === 4
})

const isLowest = computed(() => {
  return contentNr.value === 1
})
const handleBackClick = () => {
  contentNr.value--
}
const handleForwardClick = () => {
  contentNr.value++
}
</script>

<template>
  <ElementWrapper class="place-content-center">
    <AppButtonCircled
      :class="[isLowest ? 'bg-slate-300' : 'bg-slate-400']"
      v-on="isLowest ? {} : { click: handleBackClick }"
    >
      <ArrowLeftIcon />
    </AppButtonCircled>
    <AppButtonCircled
      :class="[isHighest ? 'bg-slate-300' : 'bg-slate-400']"
      v-on="isHighest ? {} : { click: handleForwardClick }"
    >
      <ArrowRightIcon />
    </AppButtonCircled>
  </ElementWrapper>
</template>

<style scoped></style>
