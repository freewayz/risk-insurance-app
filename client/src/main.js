import Vue from 'vue'
import Http from '@/utils/http'
import VueAxios from 'vue-axios'
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import './index.css'
import App from './App'
import router from './router'

Vue.config.productionTip = false

Vue.use(VueAxios, Http)
Vue.use(Element)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
