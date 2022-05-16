from rest_framework import serializers
from authorization.models import User, UserAddress


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=25, min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'error': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50, min_length=4, write_only=True)
    username = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('username', 'password')


class UserAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAddress
        fields = '__all__'
