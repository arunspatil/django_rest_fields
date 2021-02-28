from django.urls import path
from .views import *

urlpatterns = [
    path(r'getAddressDetails/', view=get_address_details),
]
