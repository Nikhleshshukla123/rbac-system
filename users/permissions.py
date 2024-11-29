from rest_framework.permissions import BasePermission
from rest_framework.response import Response

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'moderator'

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'user'


class IsAdminUserOrReadOnly(BasePermission):
    """
    Custom permission to allow only admin users to edit resources.
    Read-only permissions are granted to other users.
    """

    def has_permission(self, request, view):
        # Check if the user is an admin
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True  # Read-only methods allowed for everyone
        return request.user and request.user.is_staff  # Admin users only for write methods

