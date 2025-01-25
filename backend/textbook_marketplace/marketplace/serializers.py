from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError

from .models import Textbook, User, Order 


class TextbookSerializer(serializers.ModelSerializer):
    seller = serializers.ReadOnlyField(source='seller.username')
    class Meta:
        model = Textbook
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email') # Select desired fields

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = True

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = User.objects.filter(username=username).first()

        if not user:
            raise ValidationError({'username': 'User not found'})

        # print("Password:", password)
        # print("Stored password:", user.password)

        # if not user.check_password(password):
        if not user.password == password:
            raise ValidationError({'password': 'Invalid password'})

        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return data
    
class OrderSerializer(serializers.ModelSerializer):
    buyer = serializers.ReadOnlyField(source='buyer.username')
    textbook = serializers.ReadOnlyField(source='textbook.title')
    class Meta:
        model = Order
        fields = '__all__'

