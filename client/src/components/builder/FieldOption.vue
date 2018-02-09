<template>
 <div class="mt-3">
    <div class="form-group">
        <input @keyup.enter="handleUpdateOption(option)" 
                    type="text" 
                    class="form-control form-control-sm mt-2" 
                        v-for="(option, index) in fieldOptions" 
                        v-model="option.label" :key="index"/>
    </div>
    <button class="btn btn-light btn-sm" @click="handleAddOption">Add Option</button>
 </div>
  
</template>

<script>
import { createFormFieldOptions, updateFormFieldOption } from '@/services/risk'
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
    handleUpdateOption (option) {
      updateFormFieldOption(option.id, option).then((response) => {
        this.$notify({
          text: 'Option updated successfully',
          type: 'info'
        })
      })
    },

    handleAddOption () {
      const jsonData = {
        label: 'Enter option',
        form_field: this.field.id
      }
      createFormFieldOptions(jsonData).then((response) => {
        this.fieldOptions.push(response.data)
        this.$notify({
          text: 'Option created successfully',
          type: 'info'
        })
      })
    }
  }
}
</script>
