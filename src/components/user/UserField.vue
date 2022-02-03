<template>
  <q-item>
    <q-item-section avatar>
      <q-icon color="white" :name="icon" />
    </q-item-section>
    <q-item-section>
      <q-item-label overline class="text-white" >{{ title }}</q-item-label>
      <q-item-label caption class="text-grey-13">{{ caption }}</q-item-label>
    </q-item-section>
  </q-item>
</template>

<script>
import {defineComponent} from "vue";

export default defineComponent ({
  name: "UserField",
  props: {
    title: {
      type: String,
      default: ''
    },
    caption: {
      type: String,
      default: ''
    },
    icon: {
      type: String,
      default: ''
    },
    href: {
      type: String,
      default: null
    }
  }
})
</script>

<style scoped>

</style>
