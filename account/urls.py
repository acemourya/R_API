from django.urls import path
from .views import RegistrationApiView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/register/', RegistrationApiView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh-token/', TokenRefreshView.as_view(), name='refresh_login'),
]
