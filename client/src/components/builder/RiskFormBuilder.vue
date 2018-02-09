<template>
  <div>
      <h5 class="text-center mb-3">
        {{ riskType.title }}  Form Builder
      </h5>
      <div class="mb-3 border border-primary" v-for="(field, index) in fields" :key="index">
          <field-collector :field="field"/>
      </div>

      <div class="mb-3 float-right">
          <button class="btn btn-warning" @click.prevent="handleAddField">New Field</button>
      </div>
  </div>
</template>

<script>
import { createRiskTypeFormField, getRiskType, getRiskTypeFormFields } from '@/services/risk'
import FieldCollector from './FieldCollector'
export default {
  name: 'RiskFormBuilder',
  data () {
    return {
      fields: [],
      riskType: {}
    }
  },

  components: {
    FieldCollector
  },

  created () {
    this.getRiskType()
  },

  methods: {
    getRiskType () {
      const riskTypeId = this.$route.params.riskId
      getRiskType(riskTypeId).then((response) => {
        this.riskType = response.data
        this.getAllRiskFormField(riskTypeId)
      })
    },

    getAllRiskFormField (riskId) {
      getRiskTypeFormFields(riskId).then((response) => {
        this.fields = response.data
      })
    },

    handleAddField (event) {
      const newField = {
        label: 'New Field',
        field_type: 'TEXT',
        risk_type: this.riskType.id
      }
      createRiskTypeFormField(newField).then((response) => {
        this.fields.push(response.data)  
        this.$notify({
          text: 'New risk field added'
        })
      }).catch((err) => {
        this.$notify({
          text: 'Error creating field. Try again'
        })
      })
    }
  }
}
</script>
