from rest_framework import permissions


class RegionPermission(permissions.BasePermission):

    def __init__(self) -> None: ...

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request, view):
        return True


class DistrictPermission(permissions.BasePermission):

    def __init__(self) -> None: ...

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request, view):
        return True
