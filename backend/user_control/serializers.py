from rest_framework import serializers
from .models import CustomUser, Roles, UserActivities

class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    fullname = serializers.CharField()
    role = serializers.ChoiceField(Roles)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(required=False)
    is_new_user = serializers.BooleanField(default=False, required=False)

class UpdatePasswordSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    passwrod = serializers.CharField()

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        exclude = ("password", )

class UserActivititiesSeralizer(serializers.ModelSerializer):

    class Meta:
        model = UserActivities()
        fields = ("__all__")
