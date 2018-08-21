from rest_framework import permissions
from controller.models import Supplier


class SupplierAccessPermission(permissions.BasePermission):
    """
    工长的访问权限
    """
    def has_permission(self, request, view):
        is_supplier = Supplier.objects.filter(user__id=request.user.id).exists()
        return is_supplier
