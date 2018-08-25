<template>
  <el-date-picker type="date" placeholder="Pick a date" v-model="field" style="width: 100%;"/>
</template>

<script>
export default {
  name: 'DatePicker',
  props: ['field']
}
</script>
