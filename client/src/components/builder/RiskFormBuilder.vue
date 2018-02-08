<template>
  <div class="container">
      Risk Form Builder
      <div class="mb-3" v-for="(field, index) in fields" :key="index">
          <field-collector :field="field"/>
      </div>

      <div>
          <button class="btn btn-info btn-sm" @click.prevent="handleAddField">Add Field</button>
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
