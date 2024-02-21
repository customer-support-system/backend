from rest_framework import serializers
from.models import Issues,Levels,Solution,Staff
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from djoser import views


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model=Issues
        fields=["id","institution_name","email","issue"]


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model=Levels
        fields=["name"]


class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Solution
        fields=['id','issue_id','answer']


class StaffSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model=Staff
        fields='__all__'



class CustomTokenObtainPairSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)

            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')

            if not user.is_active:
                msg = 'User account is disabled.'
                raise serializers.ValidationError(msg, code='authorization')

            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'is_superuser': user.is_superuser  # Include is_superuser field in response
            }
            return token
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')








