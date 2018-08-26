import http from '@/utils/http'

const LOGIN_URL = '/account/login/'
const REGISTER_URL = '/account/register/'

export const login = (data) => http.post(LOGIN_URL, data)
export const register = (data) => http.post(REGISTER_URL, data)
