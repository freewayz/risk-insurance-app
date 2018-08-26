<template>
  <el-date-picker type="date" placeholder="Pick a date" v-model="userResponse" style="width: 100%;"/>
</template>

<script>
export default {
  name: 'DatePicker',
  props: ['field'],
  data () {
    return {
      userResponse: ''
    }
  }

}
</script>
