<template>
      <el-container>
        <div class="create-risk__panel">
          <h3 class="text-center">CREATE RISK TYPE</h3>
          <el-form>
              <el-form-item label="Risk title">
                  <el-input v-model="model.title"/>
              </el-form-item>

              <el-form-item label="Risk description">
                  <el-input type="text" v-model="model.description"/>
              </el-form-item>

              <el-button type="primary" :loading="loading"  @click.prevent="handleSaveRiskType">Start building</el-button>
          </el-form>
          </div>
      </el-container>
</template>

<script>
import { createRiskType } from '@/services/risk'
export default {
  name: 'CreateRiskForm',
  data () {
    return {
      loading: false,
      model: {}
    }
  },
  methods: {
    handleSaveRiskType () {
      this.loading = true
      createRiskType(this.model).then((response) => {
        const riskTypeTitle = this.model.title
        this.loading = false
        this.$notify({
          text: `Risk ${riskTypeTitle} created successfully!`
        })
        this.$router.push({name: 'Risk'})
      }).catch((error) => {
        this.loading = false
        this.$notify({
          text: 'Error creating risk type',
          type: 'error'
        })
      })
    }
  }
}
</script>

<style type="text/css" scoped>
.create-risk__panel {
  display: flex;
  flex-direction: column;
  width: 70%;
  margin: 0 auto;
}
</style>
