<template>
        <select @change="select"
        :data-type="type">
          <option value=""></option>
          <option :value="item.code"
          v-for="(item, idx) in options" :key="idx"
          >{{item.name}}</option>
        </select>
</template>

<script>
import EventBus from '../EventBus.js'

export default {
  name: 'TransactionType',
  props: ['type', 'transactionTypes'],
  data () {
    return {
    }
  },
  methods: {
    select: function (e) {
      let value = e.target.value
      let type = e.target.dataset.type
      let data = {type: type, value: value}
      EventBus.$emit('type-selected', data)
    }
  },
  computed: {
    options: function () {
      return this.transactionTypes
    }
  },
  created () {
  }
}

</script>

<style scoped>

</style>
