<template>
  <el-container>
      <h3 class="">
           {{ riskType.title }}
      </h3>
      <p>{{ riskType.description }}</p>

      <el-form v-if="riskTypeFields.length > 0" style="width: 100%">
          <form-field v-for="(field, index) in riskTypeFields" :key="index" :field="field"/>
          <el-button >Save Information</el-button>
      </el-form>
      <div v-else>
        No Form has been configured for this risk type
      </div>
  </el-container>
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
