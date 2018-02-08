"""
    API Test cases for Risk
"""
__autho__ = "peter"
from rest_framework.test import APITestCase
from .models import ( RiskType, RiskFormField, FIELD_TYPES)
from model_mommy import mommy
import json

class RiskTypeAPITestCase(APITestCase):
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
        mommy.make(RiskType, _quantity=3)
        response = self.client.get(path=self.url)
        items = json.loads(response.content)
        self.assertEqual(len(items), 3)



class RiskTypeFormAPITestCase(APITestCase):
    url = "risk/types/fields"
    data = {
        'label': 'Housing Number',
        'field_type': 'NUMBER',
    }

    def setUp(self):
        # let mock a single risk type as our foreign key
        self.risktype = mommy.make(RiskType)

    def test_that_insurer_can_create_risktype_form_data(self):
        self.data['risk_type'] = self.risktype.pk
        response = self.client.post(
            path=self.url,
            data=self.data
        )
        self.assertEqual(response.status_code, 201)
