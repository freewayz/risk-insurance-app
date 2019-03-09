/* global localStorage */
import axios from 'axios'

function getApiDomain () {
  if (process.env.NODE_ENV === 'development') {
    return 'http://127.0.0.1:8000'
  }
  // this code is a production code
  return `https://4ur9bc8036.execute-api.us-east-1.amazonaws.com/dev`
}
const Http = axios.create({
  baseURL: getApiDomain()
})

const userToken = localStorage.getItem('_UFO')
if (userToken) {
  Http.defaults.headers.common.Authorization = `Token ${userToken}`
}

export default Http
