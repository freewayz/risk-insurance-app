import Vue from 'vue'
import Router from 'vue-router'
import Risk from '@/components/Risk'
import RiskForm from '@/components/RiskForm'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Risk',
      component: Risk
    },
    {
      path: '/risk/:id/form/',
      name: 'RiskForm',
      component: RiskForm
    }
  ]
})
