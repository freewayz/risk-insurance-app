from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from .serializers import (
    RiskTypeSerializer
)
from .models import RiskType

__autho__ = "peter"

class RiskTypeAPI(viewsets.ModelViewSet):
    serializer_class  = RiskTypeSerializer
    queryset = RiskType.objects.all()
    