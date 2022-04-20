from .models import Customer,Product,Cart,OrderPlaced
from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import models
from .models import STATE_CHOICES

from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


# from rest_framework import serializers
# from django.contrib.auth.models import User

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)





# class Userserializer(serializers.Serializer):
#     class Meta:
#         model = User
#         fields="__all__"



class CustomerSerializers(serializers.Serializer):
    user = UserSerializer(read_only=True,many=True)
    state = serializers.ChoiceField(choices = STATE_CHOICES)
    class Meta:
        model = Customer
        fields = "__all__"







class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user','product','quantity']

class OrderPlacedSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderPlaced
        fields = ['user','customer','product',
                    'quantity','ordered_date','status']



