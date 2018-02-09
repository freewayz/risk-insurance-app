<template>
<div class="d-flex flex-column">
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
  </div>
  <div  v-if="isOptions">
          <field-option :field="field"/>
  </div>
</div>
</template>

<script>
import { updateRiskTypeFormField } from '@/services/risk'
import FieldOption from './FieldOption'
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

  components: {
    FieldOption,
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
