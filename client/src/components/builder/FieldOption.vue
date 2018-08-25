<template>
 <div class="field-collection__options">
    <div class="field-collection__options-input" v-for="(option, index) in fieldOptions" :key="index">
        <el-input size="mini"
          v-on:change="handleUpdateOption(option)"
          type="text"
          placeholder="Field name"
          style="margin-right: 5px;"
          v-model="option.label"/>
        <el-button circle size="mini" type="danger"  class="el-icon-delete"/>
    </div>
    <div>
      <el-button type="primary" plain size="mini" icon="el-icon-circle-plus-outline"  @click="handleAddOption">
        Add option
      </el-button>
    </div>
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
      console.log('@@Changes', option)
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

<style scoped>
.field-collection__options {
  width: 60%;
}
.field-collection__options-input {
  display: flex;
  flex-direction: row;
  margin: 5px 0;
  align-items: center;
  justify-content: space-between;
}
</style>
