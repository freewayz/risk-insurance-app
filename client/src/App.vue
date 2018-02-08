<template>
  <div id="app">
      <ul class="nav justify-content-center">
        <li class="nav-item">
          <a class="nav-link active" href="#">BritCore</a>
        </li>
        <li class="nav-item">
          <router-link :to="{name: 'Risk'}" class="nav-link" >Risk Types</router-link>
        </li>
     </ul>
    <notifications  />
    <div class="container w-50 mx-auto">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: "App"
};
</script>


