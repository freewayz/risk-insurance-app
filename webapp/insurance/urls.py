from django.urls import path, include

urlpatterns = [
    path('risk/', include('risk.urls')),
    path('account/', include('account.urls')),
]
