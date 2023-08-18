from rest_framework import permissions


class IsUserOrGetOrPostOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_anonymous:
            return obj == request.user


class IsUserProfileOrGetOrPostOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_anonymous:
            return obj.user == request.user


from rest_framework.authentication import TokenAuthentication


class CustomTokenAuthentication(TokenAuthentication):
    def has_permission(self, request, view):
        return True
