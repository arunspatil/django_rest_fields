from django.urls import path
from .views import *

urlpatterns = [
    path(r'create_list/', view=create_list_data),
]
