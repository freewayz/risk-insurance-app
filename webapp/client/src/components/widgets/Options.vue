<template>
    <div>
        <label for=""> {{ label }}</label>
        <div v-for="(op, index) in options" :key="index">
            <input type="radio">
        </div>
    </div>
</template>

<script>
export default {
  name: 'OptionsInput',
  props: ['options', 'label', 'type']
}
</script>
