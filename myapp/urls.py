from django.urls import path
from .views import RegisterView, UserProfileView, DashboardView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', UserProfileView.as_view(), name='user_profile'),
     path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
