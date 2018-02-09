<template>
  <div id="app" class="mx-auto">
      <ul class="nav justify-content-center bg-light">
        <li class="nav-item">
          <a class="nav-link active" href="https://britcore.com">BRITCORE</a>
        </li>
        <li class="nav-item">
          <router-link  :to="{name: 'Risk'}" class="nav-link" >RISK</router-link>
        </li>
        <li class="nav-item">
          <router-link  :to="{name: 'CreateRisk'}" class="nav-link" >CREATE RISK</router-link>
        </li>
     </ul>
    <div class="mt-4 container card brit-content">
     <div class="justify-content-center">
        <notifications  />       
       <div class="p-3">
        <router-view/>
       </div>
     </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style scoped>
  .brit-content {
    width: 40% !important;
  }
</style>
