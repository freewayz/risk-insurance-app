from rest_framework.routers import DefaultRouter
from .apis import RiskTypeAPI

router = DefaultRouter()
router.register(r'types', viewset=RiskTypeAPI, base_name='type')

urlpatterns = router.urls