<template>
  <section>
      <div>
          Create Risk Form

          <form>
              <div>
                  <label for="">Risktype Title</label>
                  <input type="text"  v-model="model.title" required> 
              </div>

              <div>
                  <label for="">RiskType Description</label>
                  <input type="text" v-model="model.description">
              </div>

              <div>
                  <button>Save</button>
                  <button>Save and Create Form</button>
              </div>
          </form>
      </div>
  </section>
</template>


<script>
export default {
  name: 'CreateRiskForm',
  data () {
    return {
      model: {}
    }
  },
  methods: {
    saveRiskType () {} 
  }
}
</script>
