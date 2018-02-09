import http from '@/utils/http'

const URLS = {
  TYPE: '/types/',
  FIELDS: '/form-fields/',
  FIELDS_OPITON: '/form-fields-options/'
}

export function createRiskType (data) {
  return http.post(URLS.TYPE, data)
}

export function getRiskType (riskId) {
  return http.get(`${URLS.TYPE}${riskId}/`)
}

export function getRiskTypes () {
  return http.get(URLS.TYPE)
}

export function createRiskTypeFormField (data) {
  return http.post(URLS.FIELDS, data)
}

export function updateRiskTypeFormField (id, data) {
  return http.put(`${URLS.FIELDS}${id}/`, data)
}

export function getRiskTypeFormFields (riskTypeId) {
  const apiUrl = `${URLS.TYPE}${riskTypeId}/form_fields/`
  return http.get(apiUrl)
}

export function createFormFieldOptions (data) {
  return http.post(URLS.FIELDS_OPITON, data)
}

export function updateFormFieldOption (id, data) {
  return http.put(`${URLS.FIELDS_OPITON}${id}/`, data)
}
