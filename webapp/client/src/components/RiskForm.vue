<template>
  <section>
      <div>
          Risk Form
      </div>
      <div v-if="riskTypeFields.length > 0">
        <div v-for="(field, index) in riskTypeFields" :key="index">
          <form-field :field="field"/>
        </div>
      </div>

      <div v-else>
        No Form has been configured for this risk type
      </div>
      
  </section>
</template>

<script>
import { getRiskTypeFormFields, getRiskType } from '@/services/risk'
import FormField from './FormField'

export default {
  name: 'RiskForm',
  data () {
    return {
      riskType: {},
      riskTypeFields: []
    }
  },
  components: {
    FormField
  },
  mounted () {
    this.onGetRiskType()
  },
  methods: {
    onGetRiskType () {
      const riskTypeId = this.$route.params.riskId
      getRiskType(riskTypeId).then((response) => {
        this.riskType = response.data
        this.getAllRiskFormField(riskTypeId)
      })
    },

    getAllRiskFormField (riskId) {
      getRiskTypeFormFields(riskId).then((response) => {
        this.riskTypeFields = response.data
      })
    }
  }
}
</script>
