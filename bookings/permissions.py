from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Safe methods: GET, HEAD, OPTIONS → allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only allowed to owner of the review
        return obj.traveler == request.user
