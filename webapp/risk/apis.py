from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.generics import ListAPIView
from .serializers import (
    RiskTypeSerializer, RiskFormFieldSerializer,
    RiskFormFieldOptionSerializer
)
from .models import (
    RiskType, RiskFormField, RiskFormFieldOption
)

__autho__ = "peter"

class RiskTypeAPI(viewsets.ModelViewSet):
    serializer_class  = RiskTypeSerializer
    queryset = RiskType.objects.all()

    @detail_route(methods=['get'])
    def form_fields(self, request, pk):
        risk_type = get_object_or_404(RiskType, pk=pk)
        form_fields = RiskFormField.objects.filter(risk_type=risk_type)
        serialized_data = RiskFormFieldSerializer(instance=form_fields, many=True)
        return Response(
            data=serialized_data.data, 
            status=HTTP_200_OK
        )
    

class FormFieldAPI(viewsets.ModelViewSet):
    serializer_class = RiskFormFieldSerializer
    queryset = RiskFormField.objects.all()

    @detail_route(methods=['get'])
    def form_options(self, request, pk):
        form_field = get_object_or_404(RiskFormField, pk=pk)
        field_options = RiskFormFieldOption.objects.filter(form_field=form_field)
        serialized_data = RiskFormFieldOptionSerializer(instance=form_fields, many=True)
        return Response(
            data=serialized_data.data, 
            status=HTTP_200_OK
        )

class FormFieldOptionAPI(viewsets.ModelViewSet):
    serializer_class = RiskFormFieldOptionSerializer
    queryset = RiskFormFieldOption.objects.all()
