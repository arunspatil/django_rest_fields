from django.urls import path
from .views import *

urlpatterns = [
    path(r'get_all_operations/', view=get_all_operations),
    path(r'create_operations/', view=create_operations),
    path(r'delete_all_operations/', view=delete_all_operations),
    path(r'delete_operations/', view=delete_operations),
]