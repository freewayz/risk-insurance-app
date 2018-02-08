<template>
    <div class="form-group">
        <label for=""> {{ field.label }}</label>
        <div v-for="(op, index) in field.options" :key="index">
            <input type="radio" :name="field.label">
        </div>
    </div>
</template>

<script>
export default {
  name: 'OptionsInput',
  props: ['field']
}
</script>
