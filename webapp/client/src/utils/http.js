import axios from 'axios'
function getApiDomain () {
  if (process.env.NODE_ENV === 'development') {
    return 'http://127.0.0.1:8000/risk'
  }
  // this code is a production code
  const clientName = window.location.hostname
  return `${window.location.protocol}//${clientName}/risk`
}
const Http = axios.create({
  baseURL: getApiDomain()
})

export default Http
