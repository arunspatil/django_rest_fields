from django.urls import path
from .views import (
    get_all_operations,
    create_operation,
    delete_all_operations,
    delete_operation
)

urlpatterns = [
    path(r'get_all_operations/', view=get_all_operations),
    path(r'create_operations/', view=create_operations),
    path(r'create_operation/', view=create_operation),
    path(r'delete_all_operations/', view=delete_all_operations),
    path(r'delete_operation/', view=delete_operation),
]
