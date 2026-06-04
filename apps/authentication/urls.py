from django.urls import path
from .views import (RegisterView, LoginView, ProfileView)

urlpatterns = [
    path('signals/register/', RegisterView.as_view(), name="register"),
    path('signals/login/', LoginView.as_view(), name="login"),
    path('signals/profile/<int:profile_id>/', ProfileView.as_view(), name="profile")

]