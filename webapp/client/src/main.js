import Vue from 'vue'
import Http from '@/utils/http'
import VueAxios from 'vue-axios'
import VueNotification from 'vue-notification'
import App from './App'
import router from './router'

Vue.config.productionTip = false

Vue.use(VueAxios, Http)
Vue.use(VueNotification)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
