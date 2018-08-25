<template>
  <el-container>
    <div class="auth-panel">
      <el-card>
        <el-row>
          <el-col :span="10">
            <div>
              BRITCORE RISK INSURANCE APP
            </div>
          </el-col>
          <el-col :span="14">
            <el-form  size="small" label-position="top" label-width="100px">
              <el-form-item label="Username">
                <el-input v-model="model.username" placeholder="Provide username"/>
                </el-form-item>
                <el-form-item label="Password">
                  <el-input v-model="model.password"/>
                  </el-form-item>

                  <el-button size="small" @click="onLogin" type="primary" icon="el-icon-forward" >Login </el-button>
                  <el-button type="text" size="mini" plain> Don't have an account </el-button>
                </el-form>
              </el-col>
            </el-row>
          </el-card>
    </div>
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

<style type="text/css" scoped>
.auth-panel {
  margin: 0 auto;
  width: 70%;
}
</style>
