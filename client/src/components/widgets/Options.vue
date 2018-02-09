<template>
    <div class="form-group">
        <label for=""> {{ field.label }}</label>
        <div class="col-sm-12">
            <div class="form-check" v-for="(opt, index) in field.options" :key="index">
            <input class="form-check-input" :id="index + opt.label"  type="radio" :name="field.label">
            <label :for="index + opt.label" class="form-check-label">
                {{ opt.label }}
            </label>
        </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'OptionsInput',
  props: ['field']
}
</script>
