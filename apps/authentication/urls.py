from django.urls import path
from .views import (RegisterView, LoginView)

urlpatterns = [
    path('signals/login/', RegisterView.as_view(), name="login"),
    path('signals/register/', LoginView.as_view(), name="register"),

]