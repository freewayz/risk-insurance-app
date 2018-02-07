from django.test import TestCase
from .models import ( RiskType, RiskFormField, RiskFormFieldOption)
from model_mommy import mommy

class RiskTypeTestCase(TestCase):
    title = 'Peters Home Insurance Risk'

    def setUp(self):
        self.mocked_risk_type = mommy.make(RiskType, **{
            'title': self.title
        })

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
    pass