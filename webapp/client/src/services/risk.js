import http from '@/utils/http'

const URLS = {
  TYPE: '/types/',
  FIELDS: '/form-fields/'
}

export function createRiskType (data) {
  return http.post(URLS.TYPE, data)
}

export function getRiskTypes (data) {
  return http.get(URLS.TYPE)
}

export function createRiskTypeFormField (data) {
  return http.post(URLS.FIELDS, data)
}

export function getRiskTypeFormFields (riskTypeId) {
  const apiUrl = `${URLS.TYPE}${riskTypeId}/form_field/`
  return http.get(apiUrl)
}
