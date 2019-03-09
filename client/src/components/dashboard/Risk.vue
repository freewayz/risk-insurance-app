<template>
  <div>
    <div style="margin-top: 20px">
    <h3 class="text-center">RISK</h3>
    <el-radio-group v-model="filterType" size="small">
      <el-radio-button label="null">Only Me</el-radio-button>
      <el-radio-button label="by_all">Everywhere</el-radio-button>
    </el-radio-group>
  </div>
    <div  v-if="riskItems.length > 0" class="list-group">
      <el-table :data="riskItems" style="width: 100%">
        <el-table-column
                                  prop="title"
                                  label="Title"
                                  width="400">
        </el-table-column>
        <el-table-column
                                  prop="description"
                                  label="Description"
                                  width="300">
        </el-table-column>
        <el-table-column
                                  fixed="right"
                                  label="Operations"
                                  width="200">
          <template slot-scope="scope">
            <el-button @click="gotoEdit(scope.row)" type="text" size="small">Edit</el-button>
            <el-button @click="gotoPreview(scope.row)" type="text" size="small">Preview</el-button>
            <el-button @click="gotoBuilder(scope.row)" type="text" size="small">Customize</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div v-else>
      <h1>You have not created any RISK FORM start building one now</h1>
    </div>
  </div>
</template>

<script>
import { getRiskTypes } from '@/services/risk'
export default {
  name: 'Risk',
  data () {
    return {
      riskItems: [],
      filterType: ''
    }
  },
  watch: {
    filterType (value) {
      this.fetchRisk(value)
    }
  },
  mounted () {
    this.fetchRisk(null)
  },

  methods: {
    fetchRisk (mode) {
      getRiskTypes(mode).then((response) => {
        this.riskItems = response.data
      })
    },
    gotoEdit (item) {
      this.$router.push({name: 'EditRisk', params: {id: item.id}})
    },
    gotoPreview (item) {
      this.$router.push({name: 'RiskForm', params: {riskId: item.id}})
    },

    gotoBuilder (item) {
      this.$router.push({name: 'RiskFormBuilder', params: {riskId: item.id}})
    }
  }
}
</script>

<style scoped>

</style>
