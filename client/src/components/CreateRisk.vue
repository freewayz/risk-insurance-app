<template>
  <section>
      <div>
          Create Risk Form
          <form>
              <div>
                  <label for="">Risktype Title</label>
                  <input type="text"  v-model="model.title" required> 
              </div>

              <div>
                  <label for="">RiskType Description</label>
                  <input type="text" v-model="model.description">
              </div>

              <div>
                  <button>Save</button>
                  <button @click.prevent="handleSaveRiskType">Save and Create Form</button>
              </div>
          </form>
      </div>
  </section>
</template>

<script>
import { createRiskType } from '@/services/risk'
export default {
  name: 'CreateRiskForm',
  data () {
    return {
      model: {}
    }
  },
  methods: {
    handleSaveRiskType () {
      createRiskType(this.model).then((response) => {
        const riskTypeTitle = this.model.title
        this.$notify({
          text: `Risk ${riskTypeTitle} created successfully!`
        })
      }).catch((error) => {
        this.$notify({
          text: 'Error creating risk type',
          type: 'error'
        })
      })
    }
  }
}
</script>
