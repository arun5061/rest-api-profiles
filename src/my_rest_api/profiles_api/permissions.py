from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """This class allows user to edit only their own profile else it give only view access"""
    def has_object_permission(self, request, view, obj):
        """Checking request method it allows only GET access if not return false"""
        print('request:', request.user)
        print('obj:', obj)
        print('obj.id:', obj.id)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
