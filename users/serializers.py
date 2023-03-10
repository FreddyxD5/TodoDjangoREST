from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        read_only_fields = 'created_at',


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=80)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Users
        fields = ['email','username','password']

    def validate(self, attrs):
        email_exists = Users.objects.filter(email =attrs['email']).exists()
        if email_exists:
            raise ValidationError("El email ya ha sido usado")
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user


class GetUserSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length=80)
    username = serializers.CharField(max_length=80)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = Users
        fields = ['username','email', 'password']


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=80)
    password = serializers.CharField(min_length=8, write_only=True)
    class Meta:
        model = Users
        fields = ['username','password']
