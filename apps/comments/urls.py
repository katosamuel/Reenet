from django.urls import path
from .views import CommentView

urlpatterns = [
    path('signals/<int:post_id>/comments/', CommentView.as_view(), name="login")

]