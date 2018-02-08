<template>
  <div>
      <component :is="formComponent" :field="field"/>
  </div>
</template>

<script>
import Options from './widgets/Options'
import TextInput from './widgets/TextInput'
const FIELD_TYPE = {
  TEXT: 'TEXT',
  NUMBER: 'NUMBER',
  DATE: 'DATE',
  OPTIONS: 'OPTIONS'
}
export default {
  name: 'FormField',
  props: ['field'],
  data () {
    return {
      formComponent: 'text-input'
    }
  },
  components: {
    Options,
    TextInput
  },
  mounted () {
    this.setupFormType()
  },
  methods: {
    setupFormType () {
      switch (this.field.field_type) {
        case FIELD_TYPE.TEXT:
        case FIELD_TYPE.NUMBER:
        case FIELD_TYPE.DATE:
          this.formComponent = 'text-input'
          break
        case FIELD_TYPE.OPTIONS:
          this.formComponent = 'options'
          break
        default:
          this.formComponent = 'text'
      }
    }
  }
}
</script>
