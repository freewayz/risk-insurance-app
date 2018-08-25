<template>
  <div id="app" class="app">
    <el-container>
      <el-header>
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" >
          <el-menu-item index="1" route="Risk">Dashboard</el-menu-item>
          <el-menu-item index="3">Response</el-menu-item>
          <el-menu-item index="3" route="CreateRisk">Build</el-menu-item>
        </el-menu>
      </el-header>
      <el-main>
          <router-view/>
      </el-main>
    </el-container>

  </div>
</template>

<script>
export default {
  name: 'App',
  data () {
    return {
      activeIndex: '1'
    }
  }
}
</script>

<style scoped>
.app {
  width: 70%;
  margin: auto;
}
.el-main {

}
.brit-content {
  width: 40% !important;
}

</style>
