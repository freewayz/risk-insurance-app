from rest_framework.routers import DefaultRouter
from .apis import  (
    RiskTypeAPI, 
    FormFieldAPI,
    FormFieldOptionAPI
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
router.register(
    r'form-fields-options',
    viewset=FormFieldOptionAPI,
    base_name='form-fields-options'
)

urlpatterns = router.urls