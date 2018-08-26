
from rest_framework.routers import DefaultRouter
from .apis import RegistationResource, LoginResource

router = DefaultRouter()
router.register(
    r'register',
    RegistationResource,
    base_name='register'
)
router.register(
    r'login',
    LoginResource,
    base_name='login'
)

urlpatterns = router.urls
