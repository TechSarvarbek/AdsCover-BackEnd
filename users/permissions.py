from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):
	def has_permission(self, request, view):
		if request.user.is_authenticated and request.user.active and not request.user.block:
			return True 
		else:
			return False