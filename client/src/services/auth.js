/* global localStorage */
import http from '@/utils/http'

const LOGIN_URL = '/account/login/'
const REGISTER_URL = '/account/register/'

export const login = (data) => http.post(LOGIN_URL, data)
export const register = (data) => http.post(REGISTER_URL, data)

// TODO make use of cookies for safety
export const saveToken = (token, username) => {
  localStorage.setItem('_UFO', token)
  localStorage.setItem('_AVATAR', username)
  http.defaults.headers.common.Authorization = `TOKEN ${token}`
}

export const getStorageItem = (key) => {
  return localStorage.getItem(key)
}

export const isLoggedIn = () => {
  if (getStorageItem('_UFO')) {
    const username = getStorageItem('_AVATAR')
    return Promise.resolve(username)
  }
  return Promise.reject(new Error('Token not found'))
}
