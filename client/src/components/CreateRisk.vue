<template>
      <div class="flex-column">
          <h3 class="text-center">CREATE RISK TYPE</h3>
          <form class="mt-1">
              <div class="form-row">
                  <label for="riskTitle">Risktype Title</label>
                  <input type="text" class="form-control"  id="riskTitle" v-model="model.title" required> 
              </div>

              <div>
                  <label for="riskDesc">RiskType Description</label>
                  <input type="text" class="form-control" id="riskDesc" v-model="model.description">
              </div>

              <div class="mt-2 text-right">
                  <button class="btn btn-primary" @click.prevent="handleSaveRiskType">Save and Build Form</button>
              </div>
          </form>
      </div>
</template>

<script>
import { createRiskType } from '@/services/risk'
export default {
  name: 'CreateRiskForm',
  data () {
    return {
      model: {}
    }
  },
  methods: {
    handleSaveRiskType () {
      createRiskType(this.model).then((response) => {
        const riskTypeTitle = this.model.title
        this.$notify({
          text: `Risk ${riskTypeTitle} created successfully!`
        })
        this.$router.push({name: 'Risk'})
      }).catch((error) => {
        this.$notify({
          text: 'Error creating risk type',
          type: 'error'
        })
      })
    }
  }
}
</script>
