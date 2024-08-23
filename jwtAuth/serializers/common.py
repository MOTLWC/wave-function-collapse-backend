from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password_verify = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        password_verify = data.pop("password_verify")
        password = data.pop("password")

        if password != password_verify:
            raise serializers.ValidationError({"errorMessage":"Passwords Do Not Match"})

        password_validation.validate_password(password=password)

        data["password"] = make_password(password)

        return data
    
    class Meta:
        model = get_user_model()
        fields = ("id","username","password","password_confirmation")