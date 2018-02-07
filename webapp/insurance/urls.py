from django.urls import path, include

urlpatterns = [
    path('risk/', include('risk.urls')),
]
