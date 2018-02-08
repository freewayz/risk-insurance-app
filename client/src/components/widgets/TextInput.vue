<template>
    <div>
        <label for="">
            {{ field.label }}
        </label>
        <input :type="inputType"/>
    </div>
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
