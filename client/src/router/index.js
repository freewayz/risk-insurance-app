import Vue from 'vue'
import Router from 'vue-router'
import Risk from '@/components/Risk'
import RiskForm from '@/components/RiskForm'
import RiskFormBuilder from '@/components/builder/RiskFormBuilder'
import CreateRisk from '@/components/CreateRisk'
import Login from '@/components/auth/Login'
import Register from '@/components/auth/Register'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
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
