from rest_framework.permissions import BasePermission

class IsPostOwner(BasePermission):
    message = "user is not the post owner"
    def has_object_permission(self, request, view, obj) -> bool:
        return obj.author_id == request.user.id