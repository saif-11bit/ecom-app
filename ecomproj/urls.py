from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Ecommerce API")

urlpatterns = [
    path('api/docs/', schema_view),
    path('admin/', admin.site.urls),
    path('api/', include('product.urls')),
    path('api/auth/', include('authorization.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view, name='token_refresh'),
]
