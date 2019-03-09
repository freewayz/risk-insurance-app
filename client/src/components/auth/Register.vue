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
                <el-form-item label="Email">
                  <el-input type="email" v-model="model.email" placeholder="Provide email "/>
                  </el-form-item>
                  <el-form-item label="Password">
                    <el-input type="password" v-model="model.password"/>
                    </el-form-item>

                    <el-button @click="gotoLogin" type="text" size="mini" plain> Already have an account </el-button>
                    <el-button :loading="loading" size="small" @click="onRegister" type="primary" icon="el-icon-forward" >Create my account</el-button>
                  </el-form>
                </el-col>
              </el-row>
            </el-card>
    </div>
          </el-container>
</template>

<script>
import {register} from '@/services/auth'

export default {
  name: 'Registration',
  data () {
    return {
      loading: false,
      model: {
        username: '',
        email: '',
        password: ''
      }
    }
  },

  methods: {
    onRegister () {
      this.loading = true
      register(this.model)
        .then((res) => {
          this.loading = false
          this.$notify({title: 'Registration',
            message: 'Account created successfully',
            type: 'success'
          })
          // navigate to Login page
          setTimeout(this.gotoLogin, 3000)
        })
        .catch((err) => {
          console.log(err.response.data)
          this.loading = false
          this.$notify.error({
            title: 'Registation Error',
            message: 'Server encountered an error'
          })
        })
    },

    gotoLogin () {
      this.$router.push({name: 'Login'})
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
