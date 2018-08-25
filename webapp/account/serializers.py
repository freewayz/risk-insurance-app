from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.EmailField()

    def validate(self, data):
        # check if username already exist
        try:
            User.objects.get_by_natural_key(data.get('username'))
            raise ValidationError(details={'message':'User with this username already exist'})
        except User.DoesNotExist:
            pass


        return data


    def create(self, data):
        user = User(
            username=data.get('username'),
            password=data.get('password'),
            email=data.get('email'),
            first_name='',
            last_name=''
        )

        user.save()
        return 'Created new account succesfully'

