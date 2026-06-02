from django.urls import path
from .views import (SignalView)

urlpatterns = [
    path('signals/', SignalView.as_view(), name="signals_get"),
    path('signals/<int:signal_id>/', SignalView.as_view(), name="signals_update_delete"),

]