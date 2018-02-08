from model_mommy import mommy
from .models import (
    RiskType,
    RiskFormFieldOption,
    RiskFormField
)

def mock_risk_type(title='Peters Home Insurance Risk', qty=1):
    return mommy.make(RiskType, **{
            'title': title
        })

def mock_risk_form_field():
    return mommy.make(RiskFormField, **{
        'risk_type': mock_risk_type(),
        'field_type': 'NUMBER',
    })

