<template>
  <div style="float: left">
    <div id="range-container">
      <input type="text" v-model="year" placeholder="년">
      <select name="" id="" v-model="quarter" v-if="month == 0">
        <option></option>

        <option value="1">1/4</option>
        <option value="4">2/4</option>
        <option value="7">3/4</option>
        <option value="10">4/4</option>

      </select>
      <input v-if="!quarter" type="text" v-model="month" placeholder="월">
      <button @click="updateChart">적용</button>
    </div>
    <div id="chart-container">
      <charts :attr="{'labels': '총자산', 'color': '#42b983', 'height': '200', 'type': 'budget'}" :data="budget" v-if="budget"></charts>
      <charts :attr="{'labels': '순자산', 'color': '#f1c40f', 'height': '200', 'type': 'debit'}" :data="debit" v-if="debit"></charts>
      <charts :attr="{'labels': '순부채', 'color': '#f87979', 'height': '200', 'type': 'credit'}" :data="credit" v-if="credit"></charts>

    </div>

  </div>
</template>

<script>
import Charts from '../slot/Charts'
import dateFns from 'date-fns'
import Http from '../config/Http'
import Api from '../config/Api'
import axios from 'axios'
import DateRange from '../utils/DateRange'
import _ from 'lodash'

export default {
  name: 'Proift',
  data () {
    return {
      'budget': null,
      'credit': null,
      'debit': null,
      'year': 0,
      'month': 0,
      'quarter': 0
    }
  },
  methods: {

    updateChart: function () {
      let temp = {}
      if (this.month > 0) {
        temp = DateRange.getDateRange(this.year + `-${this.month}-01`, 'month')
      } else if (this.quarter) {
        temp = DateRange.getDateRange(this.year + `-${this.quarter}-01`, 'quarter')
      } else {
        temp = DateRange.getDateRange(this.year + `-01-01`, 'year')
      }

      let firstDate = temp['first']
      let lastDate = temp['last']

      this.__getDatas(firstDate, lastDate).then((data) => {
        this.$emit('data-update', data)
      }

      )
    },
    __getDatas: async function (firstDay, lastDay) {
      let param = {'updated_at_before': lastDay, 'updated_at_after': firstDay}

      let budgetList = Http.get(Api.budget.list, {'params': param})
      let accountList = Http.get(Api.accounting.transaction, {'params': param})
      let vm = this
      const result = await axios.all([budgetList, accountList]).then(axios.spread(function (budgetResult, accResult) {
        let accData = accResult.data
        const growth = 1
        const decline = 2
        let profitGrowths = vm.__sumAmount(_.filter(accData, function (o) {
          if (o.debit_type === growth) {
            return o
          }
        }))
        let profitDecline = vm.__sumAmount(_.filter(accData, function (o) {
          if (o.credit_type === decline) {
            return o
          }
        }))
        let debitGrowths = vm.__sumAmount(_.filter(accData, function (o) {
          if (o.credit_type === growth) {
            return o
          }
        }))
        let debitDecline = vm.__sumAmount(_.filter(accData, function (o) {
          if (o.debit_type === decline) {
            return o
          }
        }))
        let grossProfit = profitGrowths - profitDecline
        let result = { 'budget': vm.__sumAmount(budgetResult.data) + grossProfit, 'debit': debitGrowths - debitDecline }
        result['credit'] = result['budget'] - result['debit']
        result['budget'] = [result['budget']]
        result['credit'] = [result['credit']]
        result['debit'] = [result['debit']]

        return result
      })).catch(function (e) {
        console.log(e)
      })
      return result
    },
    __sumAmount: function (list) {
      if (list.length > 0) {
        return _.sumBy(list, function (o) { return o.cost_amount })
      } else {
        return 0
      }
    }

  },
  components: {
    Charts
  },
  mounted: async function () {
    this.year = dateFns.format(new Date(), 'YYYY')
    let tmpRange = DateRange.getDateRange(dateFns.format(new Date(), 'YYYY-MM-DD'), 'month')
    let lastDayOfMonth = tmpRange['first']
    let firstDayOfMonth = tmpRange['last']

    console.log('lastDay', lastDayOfMonth)
    console.log('firstDay', firstDayOfMonth)
    let tmp = await this.__getDatas(firstDayOfMonth, lastDayOfMonth)
    console.dir(tmp)
    this.budget = tmp['budget']
    this.debit = tmp['debit']
    this.credit = tmp['credit']
  }
}

</script>

<style scoped>
 #chart-container{
   display: flex;
 }
</style>
