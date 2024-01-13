from rest_framework import permissions


# Can call this class anything
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # If this method returns True, then the request is authorized
        # else 403 forbidden

        # SAFE_METHODS is a tuple containing 'GET', 'OPTIONS' and 'HEAD'
        if request.method in permissions.SAFE_METHODS:
            return True

        # else check if the requesting user is the same as the object's owner
        return obj.owner == request.user


