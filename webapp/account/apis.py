from rest_framework.viewsets import ViewSet
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from .serializers import RegistrationSerializer



class RegistationResource(ViewSet):

    def create(self, request):
        register_data = RegistrationSerializer(data=request.data)
        if register_data.is_valid():
            register_data.save()

            return Response(
                data={'message': 'Registration Successfull'},
                status=HTTP_200_OK
            )
        return Response(
            data=register_data.errors,
            status=HTTP_400_BAD_REQUEST
        )

