from copy import deepcopy
from django.test import TestCase
from rest_framework.test import APITestCase


USERNAME = 'peter'
PASSWORD = '12345738Ab&'
EMAIL = 'peter@email.com'


class AccountTestCase(APITestCase):

    def setUp(self):
        self.data = {
            'username': USERNAME,
            'password': PASSWORD,
            'email': EMAIL
        }
        self.url = '/account/register/'
        self.login_url = '/account/login/'


    def test_A_http_create_account_returns_200_OK(self):
        response = self.client.post(path=self.url, data=self.data)
        self.assertEqual(response.status_code, 200)

    def test_B_http_bad_payload_return_400_during_signup(self):
        bad_data = deepcopy(self.data)
        del bad_data['username']
        response = self.client.post(path=self.url, data=bad_data)
        self.assertEqual(response.status_code, 400)
        self.assertContains(response, status_code=400, text='["This field is required."]')


    def test_C_http_login_with_right_cred_returns_token(self):
        # create a user
        self.client.post(path=self.url, data=self.data)
        login_data = deepcopy(self.data)
        del login_data['email']
        response = self.client.post(path=self.login_url, data=login_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text="token", status_code=200)

    def test_C_http_bad_cred_does_not_login(self):
        login_data = deepcopy(self.data)
        del login_data['email']
        response = self.client.post(path=self.login_url, data=login_data)
        self.assertEqual(response.status_code, 400)


