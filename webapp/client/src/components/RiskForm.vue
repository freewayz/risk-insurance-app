<template>
  <section>
      <div>
          Risk Form
      </div>

      <div v-for="(field, index) in riskTypeFields" :key="index">
          <formfield :field="field"/>
      </div>
  </section>
</template>

<script>
import FormField from './FormField'
export default {
  name: 'RiskForm',
  data () {
    return {
      riskType: {},
      riskTypeFields: []
    }
  },
  components: {
    FormField
  },
  created () {
    this.getRiskFormFields()
  },
  methods: {
    getRiskFormFields () {}
  }
}
</script>
