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

