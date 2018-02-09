<template>
  <div class="d-flex flex-column">
      <h3 class="text-center">RISK TYPE ITEMS</h3>
      <div  v-if="riskItems.length > 0" class="list-group">
        <div v-for="(risk, index) in riskItems" :key="index" class="list-group-item d-flex justify-content-between align-items-center">
          <div class="mr-2"> {{ risk.title }} </div>
          <div class="mr-2"> {{ risk.description }} </div>
          <div class="mr-2">
            <router-link class="btn btn-info btn-sm" :to="{name: 'RiskForm', params: {riskId: risk.id}}"> Display </router-link>
            <router-link class="btn btn-warning btn-sm" :to="{name: 'RiskFormBuilder', params: {riskId: risk.id}}"> Build </router-link>
          </div>
        </div>
      </div>
      <div v-else>
        No Risk Item
      </div>
  </div>
</template>

<script>
import { getRiskTypes } from '@/services/risk'
export default {
  name: 'Risk',
  data () {
    return {
      riskItems: []
    }
  },
  mounted () {
    this.fetchRisk()
  },

  methods: {
    fetchRisk () {
      getRiskTypes().then((response) => {
        this.riskItems = response.data
      })
    }
  }
}
</script>

<style scoped>

</style>
