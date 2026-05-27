from django.urls import path
from .views import (RegisterView, LoginView)

urlpatterns = [
    path('signals/register/', RegisterView.as_view(), name="login"),
    path('signals/login/', LoginView.as_view(), name="register"),

]