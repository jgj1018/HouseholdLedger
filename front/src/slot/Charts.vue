<template>
  <div class="small">
    <bar-chart :chart-data="dataset" :height="height"
               ></bar-chart>
    <button @click="fillData()">Randomize</button>
  </div>
</template>

<script>
import BarChart from './BarChart.js'

export default {
  name: 'Charts',
  components: {
    BarChart
  },
  props: ['attr', 'label', 'labels', 'data'],
  data () {
    return {
      'optionObj': {},
      'height': 200,
      'dataset': {}
    }
  },
  methods: {
    fillData: function (data) {
      let dataValue = []
      if (Array.isArray(data)) {
        dataValue = data
      }
      this.dataset = {
        labels: [this.attr.labels],
        datasets: [
          {
            backgroundColor: this.attr.color,
            data: dataValue
          }
        ]
      }
    }
  },
  mounted () {
    let height = (this.attr.height !== undefined) ? this.attr.height : this.height
    this.height = Number(height)
    this.fillData(this.data)
    let vm = this
    this.$parent.$on('data-update', function(data){
      vm.fillData(data[vm.attr.type])
    })
  }
}

</script>

<style>
  .small {
    max-width: 600px;
    margin:  150px auto;
  }
</style>
