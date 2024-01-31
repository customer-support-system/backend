from rest_framework import serializers
from.models import Issues,Levels,Solution,Staff
from djoser.serializers import TokenCreateSerializer, TokenSerializer
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



class CustomTokenSerializer(TokenCreateSerializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        attrs = super().validate(attrs)
        refresh = attrs['refresh']
        data = {'refresh': refresh}

        # Use Djoser's TokenSerializer for token refresh
        token_serializer = TokenSerializer(data=data)
        token_serializer.is_valid(raise_exception=True)
        user = token_serializer.validated_data['user']

        # Include user and other necessary data in the response
        attrs['user'] = user
        return attrs



