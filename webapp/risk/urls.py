from rest_framework.routers import DefaultRouter
from .apis import RiskTypeAPI, RiskTypeFormFieldAPI

router = DefaultRouter()
router.register(
    r'types', 
    viewset=RiskTypeAPI,
    base_name='risk-type'
    )
router.register(
        r'types/fields', 
        viewset=RiskTypeFormFieldAPI, 
        base_name='risk-type-field'
    )
urlpatterns = router.urls