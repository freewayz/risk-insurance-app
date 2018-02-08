import Vue from 'vue'
import Router from 'vue-router'
import Risk from '@/components/Risk'
import RiskForm from '@/components/RiskForm'
import RiskFormBuilder from '@/components/builder/RiskFormBuilder'
import CreateRisk from '@/components/CreateRisk'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Risk',
      component: Risk
    },
    {
      path: '/add/',
      name: 'CreateRisk',
      component: CreateRisk
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
