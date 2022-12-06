from rest_framework.generics import GenericAPIView
from rest_framework import status, response, viewsets
from django.contrib import auth

from authorization.models import UserAddress
from authorization.serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserAddressSerializer,
)


class RegisterAPiView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        data = request.data
        email = data.get('email', '')
        password = data.get('password', '')
        user = auth.authenticate(email=email, password=password)
        if user:
            # saif implement djangorestframework-simplejwt
            return response.Response(data, status=status.HTTP_200_OK)
        return response.Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserAddressView(viewsets.ModelViewSet):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializer
