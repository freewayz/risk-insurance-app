<template>
  <div>
      <label for="">Field Name</label>
      <input type="text" v-model="model.label"/>
      <select name="" id="">
        <option value="" disabled>Select Field</option>
        <option v-for="(fieldType, index) in fieldDataTypes" :key="index" value="field">
            {{ fieldType }}
        </option>
      </select>
  </div>
</template>

<script>
import { updateRiskTypeFormField } from '@/services/risk'
export default {
  name: 'FieldCollector',
  props: ['field'],
  data () {
    return {
      model: {},
      fieldDataTypes: ['TEXT', 'NUMBER', 'DATE', 'OPTIONS']
    }
  },
  mounted () {
    this.model = JSON.parse(JSON.stringify(this.field))
  },

  methods: {
    handleUpdateFormField () {
      updateRiskTypeFormField(this.model.id, this.model).then((response) => {
        this.$notify({
          text: 'Updated form field'
        })
      })
    }
  }
}
</script>
