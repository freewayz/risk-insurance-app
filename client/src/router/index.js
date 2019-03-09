import Vue from 'vue'
import Router from 'vue-router'
import Risk from '@/components/dashboard/Risk'
import RiskForm from '@/components/view/RiskForm'
import RiskFormBuilder from '@/components/builder/RiskFormBuilder'
import CreateRisk from '@/components/view/CreateRisk'
import Login from '@/components/auth/Login'
import Register from '@/components/auth/Register'
import {isLoggedIn} from '@/services/auth'
Vue.use(Router)

const router = new Router({
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
      component: Risk,
      meta: {
        auth: true
      }
    },
    {
      path: '/add/',
      name: 'CreateRisk',
      component: CreateRisk,
      meta: {
        auth: true
      }
    },
    {
      path: '/edit/:id',
      name: 'EditRisk',
      component: CreateRisk,
      meta: {
        auth: true
      }
    },
    {
      path: '/form/:riskId',
      name: 'RiskForm',
      component: RiskForm,
      meta: {
        auth: true
      }
    },
    {
      path: '/builder/:riskId',
      name: 'RiskFormBuilder',
      component: RiskFormBuilder,
      meta: {
        auth: true
      }
    }
  ]
})

// check if the page has the auth true
router.beforeEach((to, from, next) => {
  /* eslint-disable */
  if (to.matched.some(record => record.meta.auth)) {
    isLoggedIn()
      .then((response) => {
        next()
      }).catch((error) => {
        router.push('/login')
      });
  } else {
    // not protected always call next to navigate to the page
    next();
  }
})


export default router
