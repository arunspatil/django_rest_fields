from django.urls import path
from .views import *

urlpatterns = [
    path(r'append/', view=list_append_view),
    path(r'extend/', view=list_extend_view),
    path(r'slicing/', view=list_slicing_view),
    path(r'copy/', view=list_copy_view),
    path(r'count/', view=list_count_view),
    path(r'index/', view=list_index_view),
    path(r'insert/', view=list_insert_view),
    path(r'reverse/', view=list_reverse_view),
    path(r'sort/', view=list_sort_view),
    path(r'substraction/', view=list_substraction_view),
    path(r'remove/', view=list_remove_view),
    path(r'clear/', view=list_clear_view),
]
