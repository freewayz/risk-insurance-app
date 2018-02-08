import axios from 'axios'


const URLS = {
  TYPE:   '/risk/types/',
  FIELDS: '/risk/form-fields/'
}


export function createRiskType(data) {
    return axios.post(URLS.TYPE, data)
}

export function getRiskType(data) {
    return axios.get(URLS.TYPE)
}

export function createRiskTypeFormField(data) {
    return axios.post(URLS.FIELDS, data);
}

export function getRiskTypeFormFields(riskTypeId) {
    const apiUrl = `${URLS.TYPE}${riskTypeId}/form_field/`
    return axios.get(apiUrl);
}