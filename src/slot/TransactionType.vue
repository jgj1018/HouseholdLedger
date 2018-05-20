<template>
        <select @change="select"
        :data-type="type">
          <option value=""></option>
          <option :value="item"
          v-for="(item, idx) in options" :key="idx"
          >{{item}}</option>
        </select>
</template>

<script>
import EventBus from '../EventBus.js'

export default {
  name: 'TransactionType',
  props: ['type'],
  data () {
    return {
      transactionTypes: {
        'credit': [1, 2, 3],
        'debit': [4, 5, 6]
      }
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
      return this.transactionTypes[this.type]
    }
  },
  created () {
  }
}

</script>

<style scoped>

</style>
