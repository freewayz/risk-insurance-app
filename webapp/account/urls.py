
from rest_framework.routers import DefaultRouter
from .apis import RegistationResource

router = DefaultRouter()
router.register(
    r'register',
    RegistationResource,
    base_name='register'
)

urlpatterns = [

]

urlpatterns += router.urls
