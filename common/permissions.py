from rest_framework.permissions import BasePermission

class IsOwnerOrManagerOrSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.role == 'owner':
            return True
        
        if user.role == 'manager':
            return obj.owner.role == 'employee'
        
        return obj.owner == user
    

class IsOwnerRole(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role == 'owner'