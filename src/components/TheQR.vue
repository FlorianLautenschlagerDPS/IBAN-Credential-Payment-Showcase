<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from 'vue'

const name = defineModel('name')
const iban = defineModel('iban')
const contentNr = defineModel('contentNr', { type: Number, required: true })

const qrSVG = ref('')
const id = ref('')
const url = ref('')
let timer
onMounted(async () => {
  const response = await fetch(`/api/requestVerifiableCredential`)
  console.log(response)
  if (response.ok) {
    const data = await response.json()
    console.log(data)
    qrSVG.value = data.qrcode
    id.value = data.transactionId
    url.value = data.url
  } else {
    // TODO: do something
  }
  timer = setInterval(async () => {
    const response = await fetch(`/api/getVerifiableCredential?id=${id.value}`)
    console.log(response)
    if (response.ok) {
      const data = await response.json()
      if (data.status === 'SUCCESS') {
        iban.value = data.claims.iban
        name.value = data.claims.name
        contentNr.value++
      }
    }
  }, 1000)
})

onBeforeUnmount(() => {
  clearInterval(timer)
})
</script>

<template>
  <div>
    <div class="svg_class" target="”_blank”">
      <a :href="url" v-html="qrSVG"></a>
    </div>
  </div>
</template>

<style scoped>
.svg_class {
  width: 20rem;
  display: block;
}
</style>
