<template>
      <el-container>
        <div class="create-risk__panel">
          <h3 class="text-center"> {{isUpdating ? 'UPDATE RISK INFO': 'CREATE RISK FORM'}} </h3>
          <el-form>
              <el-form-item label="Risk title">
                  <el-input v-model="model.title"/>
              </el-form-item>

              <el-form-item label="Risk description">
                  <el-input type="text" v-model="model.description"/>
              </el-form-item>

              <el-button type="primary" :loading="loading" icon='el-icon-tickets' @click.prevent="handleSaveRiskType">
                {{ isUpdating ? 'Update and continue building' : 'Start building' }}
              </el-button>
              <el-button type="plain" @click.prevent="onCloseForm"> Cancle </el-button>
          </el-form>
          </div>
      </el-container>
</template>

<script>
import {
  createRiskType,
  getRiskType,
  updateRiskType
} from '@/services/risk'
export default {
  name: 'CreateRiskForm',
  data () {
    return {
      loading: false,
      isUpdating: false,
      model: {}
    }
  },

  mounted () {
    // check if the user is trying to update the ui
    const riskId = this.$route.params.id
    if (riskId) {
      this.getRiskInfo(riskId)
    }
  },
  methods: {
    getRiskInfo (id) {
      getRiskType(id)
        .then((res) => {
          this.model = res.data
          this.isUpdating = true
        })
        .catch((err) => {
          this.$notify.error({
            title: 'No Record Found',
            message: 'Risk with this Id not found on our system'
          })
        })
    },
    handleSaveRiskType () {
      this.loading = true
      const httpAction = this.isUpdating ? updateRiskType(this.model.id, this.model) : createRiskType(this.model)
      httpAction.then((response) => {
        const riskTypeTitle = this.model.title
        this.loading = false
        this.$notify({
          text: `Risk ${riskTypeTitle} created successfully!`
        })
        this.model = {}
        this.isUpdating = false
        this.$router.push({name: 'RiskFormBuilder', params: {riskId: response.data.id}})
      }).catch((error) => {
        this.loading = false
        this.$notify({
          text: 'Error creating risk type',
          type: 'error'
        })
      })
    },

    onCloseForm () {
      this.isUpdating = false
      this.model = {}
      this.$router.push({name: 'Risk'})
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
