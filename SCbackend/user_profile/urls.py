from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from . import views


urlpatterns = [
    path('<str:wallet_address>/', views.UserProfileDetails.as_view(), name='user-details'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
]