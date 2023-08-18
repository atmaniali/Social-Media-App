from rest_framework import permissions


class IsOutherOnlyOrGetOrPost(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_anonymous:
            return obj.author.user == request.user

        return False


class IsAuthorCommentOnlyOrGetOrPost(permissions.BasePermission):
    """
    Customise permission to let only owner of comment to update or delete
    accept get request to see comment and allow to create new comment
    """

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_anonymous:
            return obj.author.user == request.user

        return False
