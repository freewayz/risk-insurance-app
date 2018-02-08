from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from .serializers import (
    RiskTypeSerializer, RiskFormFieldSerializer
)
from .models import (
    RiskType, RiskFormField
)

__autho__ = "peter"

class RiskTypeAPI(viewsets.ModelViewSet):
    serializer_class  = RiskTypeSerializer
    queryset = RiskType.objects.all()
    

class RiskTypeFormFieldAPI(ListCreateAPIView):
    serializer_class = RiskFormFieldSerializer
    queryset = RiskFormField.objects.all()