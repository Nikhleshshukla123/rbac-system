from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'moderator'

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'user'
