<template>
  <div>
      <h1 class="h1">
        Form Builder
      </h1>
      <div class="mb-3 border border-primary" v-for="(field, index) in fields" :key="index">
          <field-collector :field="field" v-on:remove="removeFromParent"/>
      </div>

      <div class="mb-3 float-right">
          <el-button type="primary" size="small" icon="el-icon-plus" @click.prevent="handleAddField">Add Field</el-button>
      </div>
  </div>
</template>

<script>
import {
  createRiskTypeFormField,
  getRiskType,
  getRiskTypeFormFields } from '@/services/risk'
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
          title: 'New risk field added'
        })
      }).catch((err) => {
        this.$notify({
          title: 'Error creating field. Try again'
        })
      })
    },

    removeFromParent (field) {
      this.fields = this.fields.filter(f => f.id !== field.id)
    }

  }
}
</script>

<style type="text/css" scoped>

</style>
