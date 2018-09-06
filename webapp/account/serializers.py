from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()

    def validate(self, data):
        # check if username already exist
        try:
            User.objects.get_by_natural_key(data.get('username'))
            raise ValidationError(detail={'message':'User with this username already exist'})
        except User.DoesNotExist:
            pass


        return data


    def create(self, data):
        user = User.objects.create(
            username=data.get('username'),
            password=data.get('password'),
            email=data.get('email'),
            first_name='',
            last_name=''
        )
        user.set_password(data.get('password'))
        user.save()

        Token.objects.get_or_create(user=user)
        return 'Created new account succesfully'


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get_by_natural_key(username=data.get('username'))
        except User.DoesNotExist:
            raise ValidationError(
                detail='User with this account not found'
            )

        if user.check_password(data.get('password')):
            return data

        raise ValidationError(
            detail='Username or password incorrect'
        )

    def create(self, data):
        user = User.objects.get_by_natural_key(username=data.get('username'))
        token = Token.objects.get_or_create(user=user)
        return token
