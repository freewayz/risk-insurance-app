from rest_framework.viewsets import ViewSet
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from .serializers import RegistrationSerializer, LoginSerializer



class RegistationResource(ViewSet):
    authentication_classes = ()
    permission_classes = ()
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

class LoginResource(ViewSet):
    authentication_classes = ()
    permission_classes = ()
    def create(self, request):
        login_data = LoginSerializer(data=request.data)
        if login_data.is_valid():
            user, token = login_data.save()
            return Response(data={'token': token}, status=HTTP_200_OK)
        return Response(
            data=login_data.errors,
            status=HTTP_400_BAD_REQUEST
        )

