<template>
  <div class="hello">
      Risk Items
      <div>
        <router-link :to="{name: 'CreateRisk'}">Create Risk</router-link>
      </div>
      <div class="risk-items" v-if="riskItems.length > 0">
        <div v-for="(risk, index) in riskItems" :key="index">
          <div> {{ risk.title }} </div>
          <div> {{ risk.description }} </div>
          <div>
            <router-link :to="{name: 'RiskForm', params: {riskId: risk.id}}"> View Form </router-link>
            <router-link :to="{name: 'RiskFormBuilder', params: {riskId: risk.id}}"> Build Form </router-link>
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
