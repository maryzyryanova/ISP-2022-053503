from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import AccessMixin


class StudentAccessMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if hasattr(self.request.user, "student"):
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied

class TeacherAccessMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        print(self.request.user)
        if hasattr(self.request.user, "teacher"):
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied