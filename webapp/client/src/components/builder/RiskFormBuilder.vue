<template>
  <div>
      Risk Form Builder
      <div v-for="(field, index) in fields" :key="index">
          <field-collector :field="field"/>
      </div>

      <div>
          <button @click.prevent="handleAddField">Add Field</button>
      </div>
  </div>
</template>

<script>
import FieldCollector from './FieldCollector'
export default {
  name: 'RiskFormBuilder',
  data () {
    return {
      fields: []
    }
  },

  components: {
    FieldCollector
  },

  methods: {
    handleAddField (event) {
      const newField = {
        label: 'New Field',
        field_type: 'TEXT'
      }
      this.fields.push(newField)
    }
  }
}
</script>
