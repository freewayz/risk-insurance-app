<template>
  <el-container>
    <div class="auth-panel">
      <el-card>
        <el-row>
          <el-col :span="10">
            <div class="auth-panel__info">
              <span>BRITECORE RISK INSURANCE APP</span>
              <img class="logo-img" src="https://pbs.twimg.com/profile_images/661590737864142848/YnzxcPEd_400x400.png"/>
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

                  <el-button :loading="loading" size="small" @click="onLogin" type="primary" icon="el-icon-forward" >Login </el-button>
                  <el-button type="text" size="mini" plain> Don't have an account </el-button>
                </el-form>
              </el-col>
            </el-row>
          </el-card>
    </div>
</el-container>
</template>

<script>
import {login} from '@/services/auth'

export default {
  name: 'Login',
  data () {
    return {
      loading: false,
      authError: '',
      model: {
        username: '',
        password: ''
      }
    }
  },

  methods: {
    onLogin () {
      this.loading = true
      login(this.model)
        .then((res) => {
          this.loading = false
          // navigate to dashboard
          this.$router.push({name: 'Risk'})
        })
        .catch((err) => {
          this.loading = false
          this.$notify.error({
            title: 'Login Error',
            message: 'Username or password incorrect'
          })
        })
    }
  }
}
</script>

<style type="text/css" scoped>
.auth-panel {
  margin: 0 auto;
  width: 70%;
}

.auth-panel__info {
  text-align: center;
  padding: 10px;
}

.logo-img {
  margin: 0 auto;
  width: 80%;
}
</style>
