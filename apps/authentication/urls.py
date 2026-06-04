from django.urls import path
from .views import (RegisterView, LoginView, ProfileView, MyProfileView)

urlpatterns = [
    path('signals/register/', RegisterView.as_view(), name="register"),
    path('signals/login/', LoginView.as_view(), name="login"),
    
    path('signals/my_profile/', MyProfileView.as_view(), name="my_profile"),

    path('signals/profile/<int:profile_id>/', ProfileView.as_view(), name="profile")

]