<template>
  <el-card class="box-card field-collector__card">
    <el-form size="small">
      <el-row gutter=5>
        <el-col :span="18">
          <el-input label="Field name" v-on:change="handleUpdateFormField" type="text" v-model="model.label"/>
          </el-col>
          <el-col :span="6">
            <el-select @change="handleUpdateFormField"  v-model="model.field_type"
                                                        placeholder="Select Field">
              <el-option value="" disabled>Select Field</el-option>
              <el-option v-for="(fieldType, index) in fieldDataTypes" :key="index" :value="fieldType">
                {{ fieldType }}
              </el-option>
            </el-select>
          </el-col>
        </el-row>
        <el-row v-if="hasOptions" >
          <h6 class="m-2">Field Options</h6>
          <field-option :field="field"/>
        </el-row>
      </el-form>
      <div class="field-collector__card-action">
      <el-button @click="handleDeleteFormField" size="mini" icon="el-icon-delete" circle type="text"/>
      </div>
    </el-card>
</template>

<script>
import {
  updateRiskTypeFormField,
  deleteFormField
} from '@/services/risk'
import FieldOption from './FieldOption'
export default {
  name: 'FieldCollector',
  props: ['field'],
  data () {
    return {
      model: {
        field_type: ''
      },
      selectedFieldType: {},
      fieldDataTypes: ['TEXT', 'NUMBER', 'DATE', 'OPTIONS']
    }
  },

  components: {
    FieldOption
  },

  computed: {
    hasOptions () {
      if (this.model.field_type === 'OPTIONS') {
        return true
      }
      return false
    }
  },

  mounted () {
    this.model = JSON.parse(JSON.stringify(this.field))
  },

  methods: {
    handleUpdateFormField () {
      updateRiskTypeFormField(this.model.id, this.model).then((response) => {
        this.$notify({
          title: 'Updated form field'
        })
      })
    },

    handleDeleteFormField () {
      deleteFormField(this.field.id).then((res) => {
        this.$emit('remove', this.field)
        this.$notify({
          title: 'Field Removed successfully'
        })
      }).catch((err) => {
        this.$notify({
          title: 'Ooppss: Server Error'
        })
      })
    }
  }
}
</script>

<style scoped>
.field-collector__card {
  margin-bottom: 10px;
}
.field-collector__card-action {
  display: flex;
  flex-direction: row-reverse;
  margin: 3px 0;
}
</style>
