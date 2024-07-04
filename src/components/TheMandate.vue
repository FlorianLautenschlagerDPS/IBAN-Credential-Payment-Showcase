<script setup lang="ts">
const date = new Date()
const datum = `${date.getDate()}.${date.getMonth()}.${date.getFullYear()}`

const name = defineModel('name')
const iban = defineModel('iban')
const contentNr = defineModel('contentNr', { type: Number, required: true })

const handleSubmit = () => {
  contentNr.value++
}
</script>

<template>
  <div class="text-width">
    <p class="text-lg">
      MUSTER GMBH, ROSENWEG 2, 00000 IRGENDWO <br />
      Gläubiger-Identifikationsnummer DE00ZZZ1234567890 <br />
      Mandatsreferenz 66 443 <br />
    </p>
    <h2>SEPA-Lastschriftmandat</h2>
    <p>
      Ich ermächtige die Muster GmbH, EINMALIG EINE ZAHLUNG von meinem Konto mittels Lastschrift
      einzuziehen. Zugleich weise ich mein Kreditinstitut an, DIE von der Muster GmbH auf mein Konto
      GEZOGENE LASTSCHRIFT einzulösen. Hinweis: Ich kann innerhalb von acht Wochen, beginnend mit
      dem Belas-tungsdatum, die Erstattung des belasteten Betrages verlangen. Es gelten dabei die
      mit meinem Kreditinstitut vereinbarten Bedingungen.
    </p>
    <p>
      Vorname und Name (Kontoinhaber):
      <span class="bg-slate-100">{{ name }}</span>
    </p>
    <p>
      IBAN:
      <span class="bg-slate-100">{{ iban }}</span>
    </p>
    <p>IRGENDWO, {{ datum }}</p>
    <button @click="handleSubmit">Unterschrift</button>
  </div>
</template>

<style scoped>
.text-width {
  width: 50em;
}
</style>
