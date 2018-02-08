from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .apis import  (
    RiskTypeAPI, 
    RiskTypeFormFieldAPI,
    FormFieldAPI
)

router = DefaultRouter()
router.register(
    r'types', 
    viewset=RiskTypeAPI,
    base_name='risk-type'
    )
router.register(
        r'form-fields', 
        viewset=FormFieldAPI, 
        base_name='form-fields'
    )

urlpatterns = [
    url(r'(?P<risk_type_pk>[0-9]+)/form-fields/', 
    view=RiskTypeFormFieldAPI.as_view(), 
    name="risk-form-field")
]
urlpatterns += router.urls