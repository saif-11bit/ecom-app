from django.urls import path
from authorization.views import (
    RegisterAPiView,
    LoginApiView,
    UserAddressView,
)
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash=False)
router.register(r"calling-agent", UserAddressView, basename="user_address")

urlpatterns = [
    path('register', RegisterAPiView.as_view()),
    path('login', LoginApiView.as_view()),
]
