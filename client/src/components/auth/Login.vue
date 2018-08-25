<template>
  <el-container>
    <el-form size="mini">
      <el-form-item>
        <el-input v-model="model.username"/>
      </el-form-item>
      <el-form-item>
        <el-input v-model="model.password">
      </el-form-item>
    </el-form>
  </el-container>

</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      model: {
        username: '',
        password: ''
      }
    }
  },

  methods: {
    onLogin () {

    }
  }
}
</script>
