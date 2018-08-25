import {HorizontalBar, mixins} from 'vue-chartjs'
const { reactiveProp } = mixins

export default {
  extends: HorizontalBar,
  mixins: [reactiveProp],
  data () {
    return {
      'options': {
        scales: {xAxes: [{
          type: 'linear',
          position: 'bottom',
          ticks: {
            min: 100,
            stepSize: 50,
            max: 1000
          }
        }]},
        legend: {display: false},
        responsive: true,
        maintainAspectRatio: false}
    }
  },
  mounted () {
    this.renderChart(this.chartData, this.options)
  }
}
