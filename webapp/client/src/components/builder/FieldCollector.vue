<template>
  <div>
      <label for="">Field Name</label>
      <input type="text" v-model="model.label"/>
      <select name="" id="">
        <option value="" disabled>Select Field</option>
        <option v-for="(field, index) in fields" :key="index" value="field">
            {{ field }}
        </option>
      </select>
  </div>
</template>

<script>
export default {
  name: 'FieldCollector',
  data () {
    return {
      model: {},
      fields: ['TEXT', 'NUMBER', 'DATE', 'OPTIONS']
    }
  }
}
</script>
