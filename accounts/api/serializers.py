from rest_framework import serializers
from accounts.models import User, Customer
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth
from rest_framework_simplejwt.tokens import RefreshToken,TokenError

from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    confirm_password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile_no', 'password', 'confirm_password']

            
class CustomerSerializer(serializers.ModelSerializer):
    """
    A customer serializer to return the customer details
    """
    user = UserSerializer(required=True)

    class Meta:
        model = Customer
        fields = ['profile_number', 'user']

