<template>
  <el-form-item>
    <el-select v-if="field.options.length > 3" style="width: 100%;" v-model="userResponse">
      <el-option v-for="(opt, index) in field.options" :label="opt.label" :value="opt.id" :key="index"></el-option>
    </el-select>
    <el-radio-group v-else v-model="userResponse">
      <el-radio-button v-for="(opt, index) in field.options" value="opt.id" :label="opt.label" :key="index"/>
    </el-radio-group>
    </el-form-item>
</template>

<script>
export default {
  name: 'OptionsInput',
  props: ['field'],
  data () {
    return {
      userResponse: ''
    }
  }

}
</script>
