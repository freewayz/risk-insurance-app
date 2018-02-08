<template>
    <div class="form-group">
        <label for="">
            {{ field.label }}
        </label>
        <input class="form-control" :type="inputType"/>
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
