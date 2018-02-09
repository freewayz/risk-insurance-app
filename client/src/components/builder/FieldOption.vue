<template>
 <div class="form-inline">
    <div class="form-group">
        <input type="text" class="form-control sm" v-for="(option, index) in fieldOptions" v-model="option.label" :key="index"/>
    </div>
    <button class="btn btn-light btn-sm" @click="handleAddOption">Add Option</button>
 </div>
  
</template>

<script>
import { createFormFieldOptions } from '@/services/risk'
export default {
  name: 'FieldOptions',
  props: ['field'],
  data () {
    return {
      fieldOptions: []
    }
  },
  mounted () {
    if (this.field.field_type === 'OPTIONS') {
      this.fieldOptions = this.field.options || []     
    }
  },
  methods: {
    handleAddOption () {
      const jsonData = {
        label: 'Enter option'
      }
      createFormFieldOptions(jsonData).then((response) => {
        this.fieldOptions.push(response.data)
        this.$notify({
          text: 'Option created successfully',
          type: 'info'
        })
      })
    }
  },
}
</script>
