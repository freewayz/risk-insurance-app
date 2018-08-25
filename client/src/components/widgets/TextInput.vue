<template>
  <el-input :type="inputType"></el-input>
</template>

<script>
export default {
  name: 'TextInput',
  props: ['field'],
  computed: {
    inputType () {
      const fieldType = this.field.field_type
      if (fieldType === undefined || fieldType === '') {
        return ''
      }
      return fieldType.toUpperCase()
    }
  }
}
</script>
