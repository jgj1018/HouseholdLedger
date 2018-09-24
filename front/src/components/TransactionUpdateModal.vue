
<template>
  <transition name="modal-fade">
    <div class="modal-backdrop">
      <div class="modal"
        role="dialog"
        aria-labelledby="modalTitle"
        aria-describedby="modalDescription"
      >
        <header
          class="modal-header"
          id="modalTitle"
        >
          <slot name="header">
            Transaction Update
            <button
              type="button"
              class="btn-close"
              @click="closeModal"
              aria-label="Close modal"
            >
              x
            </button>
          </slot>
        </header>
        <section
          class="modal-body"
          id="modalDescription"
        >
          <slot name="body">
            <form @submit.prevent="updateTrns" >
              <input type="text" ref="trns_name" placeholder="transaction_name"/>
              <input type="text" ref="cost_amount" placeholder="cost_amount"/>
            </form>
          </slot>
        </section>
        <footer class="modal-footer">
          <slot name="footer">
            I'm the default footer!
            <button
              type="button"
              class="btn-green"
              @click="updateTrns"
            >
              Update
            </button>
          </slot>
        </footer>
      </div>
    </div>
  </transition>
</template>

<script>
import Http from '../config/Http'
import Api from '../config/Api'

export default {
  name: 'TrnsUpdateModal',
  props: ['transactionId'],
  methods: {
    updateTrns: function (event) {
      let trnsName = this.$refs.trns_name.value
      let costAmount = Number.parseFloat(this.$refs.cost_amount.value)
      let data = {}

      if (trnsName !== null && trnsName !== undefined && trnsName.length > 0) {
        data['transaction_name'] = trnsName
      }
      if (costAmount !== null && costAmount !== undefined && Number.isInteger(costAmount)) {
        data['cost_amount'] = costAmount
      }

      Http.patch(Api.accounting.update + this.transactionId + '/', data)
        .then(response => {
          this.$emit('close')
          this.$emit('renewBook')
        })
    },
    closeModal: function (event) {
      this.$emit('close')
    }
  }
}
</script>

<style>
  .modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
  }

  .modal-header,
  .modal-footer {
    padding: 15px;
    display: flex;
  }

  .modal-header {
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
  }

  .modal-footer {
    border-top: 1px solid #eeeeee;
    justify-content: flex-end;
  }

  .modal-body {
    position: relative;
    padding: 20px 10px;
  }

  .btn-close {
    border: none;
    font-size: 15px;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
  }

  .btn-green {
    color: white;
    background: #4AAE9B;
    border: 1px solid #4AAE9B;
    border-radius: 2px;
  }
</style>
