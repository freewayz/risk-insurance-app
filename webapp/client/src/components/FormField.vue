<template>
  <div>
      <component :is="formComponent"/>
  </div>
</template>

<script>
import Options from './widgets/Options'
import Text from './widgets/Text'
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
      formComponent: 'text'
    }
  },
  components: {
    Options,
    Text
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
          this.formComponent = 'text'
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
