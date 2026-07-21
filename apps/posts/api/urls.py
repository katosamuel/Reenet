from django.urls import path
from  .views import (SignalListView, SignalCreateView, SignalDetailView)

urlpatterns = [
    path('signals/', SignalListView.as_view(), name="list_signals"),
    path('signals/create/', SignalCreateView.as_view(), name="create_signal"),
    path('signals/<int:post_id>', SignalDetailView.as_view(), name="get_update_delete_signals"),
]