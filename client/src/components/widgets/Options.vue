<template>
  <el-form-item :label="field.label">
    <el-select v-if="field.options.length > 3">
      <el-option v-for="(opt, index) in field.options" :label="opt.label" :value="opt.id" :key="index"></el-option>
    </el-select>
    <el-radio-group v-else>
      <el-radio-button v-for="(opt, index) in field.options" value="opt.id" :label="opt.label" :key="index"/>
    </el-radio-group>
    </el-form-item>
</template>

<script>
export default {
  name: 'OptionsInput',
  props: ['field']
}
</script>
