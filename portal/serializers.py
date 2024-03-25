from rest_framework import serializers
from.models import Issues,Levels,Solution,Staff,CustomUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from djoser import views
from django.contrib.auth import get_user_model
from portal import constants

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model=Issues
        fields=serializers.ALL_FIELDS
        read_only_fields = ["status"]
        


class LevelSerializer(serializers.ModelSerializer):

    class Meta:
        model=Levels
        fields=serializers.ALL_FIELDS


class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Solution
        fields=['id','issue','answer']
        



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username', 'password','is_staff','is_superuser']
        extra_kwargs = {'password': {'write_only': True}}

        # password hashing

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)
    

class CustomUserSerializer(serializers.ModelSerializer):
     class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'is_staff', 'is_superuser')



class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    level_details = LevelSerializer(source="level", read_only=True) 
    
    class Meta:
        model = Staff
        fields = ['id','user','level' ,'level_details']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        level_data = validated_data.get('level') 

        if level_data is None:
            raise serializers.ValidationError("Level data is required.")
        
        # Create user
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save(is_staff=True)
        else:
            raise serializers.ValidationError(user_serializer.errors)
        
        
        # Create staff
        staff = Staff.objects.create(user=user, level=level_data)
        return staff



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
            #token expiration
            refresh.access_token.set_exp(86400) #set for 24hrs
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'is_superuser': user.is_superuser  # Include is_superuser field in response
            }
            return token
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')








