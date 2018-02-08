from django.test import TestCase
from .models import ( RiskType, RiskFormField, RiskFormFieldOption)
from .utils_test import mock_risk_type
from model_mommy import mommy




    
class RiskTypeTestCase(TestCase):
    title = 'Peters Home Insurance Risk'

    def setUp(self):
        self.mocked_risk_type = mock_risk_type()

    def test_risk_type_created_successfully(self):
        self.assertEqual(len(RiskType.objects.all()), 1, 'No risk type item was created')


    def test_that_correct_title_is_returned(self):
        expected = RiskType.objects.first()
        self.assertEqual(expected.title, self.title)
        
    def test_many_can_be_created(self):
        mommy.make(RiskType, _quantity=2)
        self.assertEqual(len(RiskType.objects.all()), 3)

    def test_update(self):
        a_risk_type = RiskType.objects.first()
        a_risk_type.title = 'Title was updated'
        a_risk_type.save()
        self.assertEqual(RiskType.objects.first().title, 'Title was updated')


class RiskFormFieldTestCase(TestCase):
    def test_that_risk_form_field_can_be_created(self):
        form_fields = mommy.make(RiskFormField, **{
            'risk_type': mock_risk_type(),
            'field_type': 'TEXT'
        })
        items = RiskFormField.objects.all()
        self.assertEqual(len(items), 1)
        form_field = items[0]
        self.assertEqual(form_field.field_type, 'TEXT')


