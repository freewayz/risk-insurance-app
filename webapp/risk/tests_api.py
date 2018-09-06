"""
    API Test cases for Risk
"""
__author__ = "peter"
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from .models import ( RiskType, RiskFormField, FIELD_TYPES)
from .utils_test import mock_risk_type, mock_risk_form_field
from model_mommy import mommy
import json

USERNAME = 'test'
PASSWORD = 'test'

class LoginMixin():
    def setUp(self):
        user = mommy.make(User, **{
            'username': USERNAME,
            'password': PASSWORD
        })
        user.set_password(PASSWORD)
        user.save()
        self.client = APIClient()
        self.client.login(username=USERNAME, password=PASSWORD)


class RiskTypeAPITestCase(LoginMixin, APITestCase):
    url = "/risk/types/"
    data = {
        "title": "Housing Risk",
        "description": "My Housing Risk information"
    }


    def test_risktype_post(self):
        response = self.client.post(path=self.url, data=self.data)
        self.assertEqual(response.status_code, 201, 'Risk was not created')
        self.assertContains(response, "Housing Risk", status_code=201)

    def test_get_all(self):
        # create some risk types
        for i in range(3):
            self.data['title'] = '{}-{}'.format(i, self.data['title'])
            self.client.post(path=self.url, data=self.data)
        response = self.client.get(path=self.url)
        items = json.loads(response.content)
        self.assertEqual(len(items), 3)



class RiskTypeFormAPITestCase(APITestCase):
    url = "/risk/form-fields/"
    data = {
        'label': 'Housing Number',
        'field_type': 'NUMBER',
    }

    def setUp(self):
        # let mock a single risk type as our foreign key
        self.risktype = mock_risk_type()

    def test_that_insurer_can_create_risktype_form_field(self):
        self.data['risk_type'] = self.risktype.pk
        response = self.client.post(
            path=self.url,
            data=self.data
        )
        self.assertEqual(response.status_code, 201)

    def test_that_risk_type_get_all_fields(self):
        self.data['risk_type'] = self.risktype.pk
        for _ in range(3):
            response = self.client.post(
                path=self.url,
                data=self.data
            )

        path = '/risk/types/{}/form_fields/'.format(self.risktype.pk)
        response = self.client.get(
            path=path
        )
        data = json.loads(response.content)
        self.assertEqual(len(data), 3)

    def test_that_field_option_returns_list(self):
        form_field =  mommy.make(RiskFormField, **{
            'risk_type': self.risktype,
            'field_type': 'NUMBER',
        })
        opt_data = {
            'label': 'This is an option'
        }
        opt_data['form_field']  = form_field.pk
        for i in range(3):
            self.client.post(
                path='/risk/form-fields-options/',
                data=opt_data
            )
        path = '/risk/types/{}/form_fields/'.format(self.risktype.pk)
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        jsonData = json.loads(response.content)
        options = jsonData[0]['options']
        self.assertEqual(len(options), 3)


class FormFieldTestCase(APITestCase):
    data = {
        'label': 'This is an option'
    }
    url = '/risk/form-fields-options/'
    def test_form_field_option_can_be_created(self):
        form_field = mock_risk_form_field()
        self.data['form_field']  = form_field.pk

        response = self.client.post(
            path=self.url,
            data=self.data
        )
        self.assertEqual(response.status_code, 201)
        self.assertContains(response, 'This is an option', status_code=201)


