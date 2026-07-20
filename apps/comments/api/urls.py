from django.urls import path
from .views import (CommentView, CommentListView)

urlpatterns = [
    path('signals/<int:post_id>/comments/<int:comment_id>', CommentView.as_view(), name="comments"),
    path('signals/<int:post_id>/comments/', CommentListView.as_view(), name="comments")
]