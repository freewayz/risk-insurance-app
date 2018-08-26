<template>
  <el-input :type="inputType" v-model="userResponse"></el-input>
</template>

<script>
export default {
  name: 'TextInput',
  props: ['field'],
  data () {
    return {
      userResponse: ''
    }
  },
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
