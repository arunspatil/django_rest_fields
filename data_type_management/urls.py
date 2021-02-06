from django.urls import path
from .views import (
    get_all_operations,
    create_operation,
    delete_operation,
    # update_operation
)

urlpatterns = [
    path('get_all_operations/', view=get_all_operations),
    path('create_operation/', view=create_operation),
    path('delete_operation/', view=delete_operation),
    # path('update-operation', view=update_operation)
]
