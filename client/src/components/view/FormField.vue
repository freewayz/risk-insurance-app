<template>
  <el-form-item :label="field.label">
      <component :is="formComponent" :field="field"/>
  </el-form-item>
</template>

<script>
import Options from '../widgets/Options'
import TextInput from '../widgets/TextInput'
import DatePicker from '../widgets/Date'
import {FIELD_TYPE} from '@/utils'

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
    TextInput,
    DatePicker
  },
  mounted () {
    this.setupFormType()
  },
  methods: {
    setupFormType () {
      switch (this.field.field_type) {
        case FIELD_TYPE.TEXT:
        case FIELD_TYPE.NUMBER:
          this.formComponent = 'text-input'
          break
        case FIELD_TYPE.DATE:
          this.formComponent = 'date-picker'
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
