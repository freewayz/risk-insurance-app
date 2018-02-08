<template>
  <div class="form-inline">
      <div class="form-group mr-2">
        <input @keyup.enter="handleUpdateFormField" class="form-control" type="text" v-model="model.label"/>
      </div>
      <select @change="handleUpdateFormField" class="form-control" v-model="model.field_type">
        <option value="" disabled>Select Field</option>
        <option v-for="(fieldType, index) in fieldDataTypes" :key="index" :value="fieldType">
            {{ fieldType }}
        </option>
      </select>

      <div v-show="isOptions">

      </div>
  </div>
</template>

<script>
import { updateRiskTypeFormField } from '@/services/risk'
export default {
  name: 'FieldCollector',
  props: ['field'],
  data () {
    return {
      model: {
        field_type: '',
      },
      selectedFieldType: {},
      fieldDataTypes: ['TEXT', 'NUMBER', 'DATE', 'OPTIONS']
    }
  },

  computed: {
    isOptions() {
      if (this.model.field_type === 'OPTIONS') {
        return true
      }
      return false
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
