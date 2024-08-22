<script setup lang="ts">
const refnr = defineModel('refnr')
const sum = defineModel('sum')
const contentNr = defineModel('contentNr', { type: Number, required: true })

const handleSubmit = (e) => {
  e.preventDefault()
  contentNr.value++
}
</script>

<template>
  <div>
    <h1>Bitte Rechnungsdaten eingeben:</h1>
    <form>
      <div>
        <label for="ref">Referenznummer/Verwendungszweck: </label>
        <input type="text" v-model="refnr" placeholder="12345" id="ref" class="bg-slate-100" />
      </div>

      <div>
        <label for="sum">Betrag: </label>
        <input
          type="number"
          v-model.number="sum"
          placeholder="0.00"
          id="sum"
          class="bg-slate-100"
        />
      </div>
      <button type="submit" @click="handleSubmit" class="bg-slate-200 rounded-md px-2 py-1">
        Weiter
      </button>
    </form>
  </div>
</template>

<style scoped></style>
