<template>
  <div class="d-flex flex-column">
      <h1 class="text-center">Risk Types</h1>
      <div class="float-right">
        <router-link class="btn btn-primary btn-sm" :to="{name: 'CreateRisk'}">Create Risk</router-link>
      </div>
      <div class="w-100" v-if="riskItems.length > 0">
        <div v-for="(risk, index) in riskItems" :key="index" class="d-flex flex-row">
          <div class="mr-2"> {{ risk.title }} </div>
          <div class="mr-2"> {{ risk.description }} </div>
          <div class="mr-2">
            <router-link class="btn" :to="{name: 'RiskForm', params: {riskId: risk.id}}"> View Form </router-link>
            <router-link class="btn" :to="{name: 'RiskFormBuilder', params: {riskId: risk.id}}"> Build Form </router-link>
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
