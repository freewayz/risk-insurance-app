import http from '@/utils/http'

const URLS = {
  TYPE: '/risk/types/',
  FIELDS: '/risk/form-fields/',
  FIELDS_OPITON: '/risk/form-fields-options/'
}

export function createRiskType (data) {
  return http.post(URLS.TYPE, data)
}

export function getRiskType (riskId) {
  return http.get(`${URLS.TYPE}${riskId}/`)
}

export function getRiskTypes (filter) {
  return http.get(`${URLS.TYPE}?filter=${filter}`)
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
export function deleteFormFieldOption (id) {
  return http.delete(`${URLS.FIELDS_OPITON}${id}/`)
}

export function deleteFormField (id) {
  return http.delete(`${URLS.FIELDS}${id}/`)
}
