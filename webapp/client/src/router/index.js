import Vue from 'vue'
import Router from 'vue-router'
import Risk from '@/components/Risk'
import RiskForm from '@/components/RiskForm'
import RiskFormBuilder from '@/components/builder/RiskFormBuilder'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Risk',
      component: Risk
    },
    {
      path: '/form/:riskId',
      name: 'RiskForm',
      component: RiskForm
    },
    {
      path: '/builder/:riskId',
      name: 'RiskFormBuilder',
      component: RiskFormBuilder
    }
  ]
})
