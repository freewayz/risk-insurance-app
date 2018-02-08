<template>
  <section>
      <div>
          Risk Form
      </div>

      <div v-for="(field, index) in riskTypeFields" :key="index">
          <form-field :field="field"/>
      </div>
  </section>
</template>

<script>
import FormField from './FormField'
const FIELDS_MOCK = [
  {
    label: 'Question Text',
    field_type: 'TEXT'
  },
  {
    label: 'Question Number',
    field_type: 'NUMBER'
  },
  {
    label: 'Question Date',
    field_type: 'DATE'
  },
  {
    label: 'Question Options',
    field_type: 'OPTIONS',
    options: [
      {
        label: 'Option 1'
      },
      {
        label: 'Option 2'
      }
    ]
  },
]
export default {
  name: 'RiskForm',
  data () {
    return {
      riskType: {},
      riskTypeFields: FIELDS_MOCK
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
