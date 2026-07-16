from django.urls import path
from  .views import (SignalListView, SignalView)

urlpatterns = [
    path('signals/', SignalListView.as_view(), name="signals_list"),
    path('signals/<int:post_id>/', SignalView.as_view(), name="signals_update_delete"),
]