from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .list import *

# Create your views here.


@api_view(['GET'])
def list_append_view(request):
    list1 = create_list()
    number = input("Enter item to be appended to the list")
    Response({"list": list_append(list1, number)}, status=status.HTTP_200_OK)


def list_extend(request, list1, list2):
    list1.extend(list2)
    return list1


def list_slicing(request, list_data, start_index, end_index, step):
    return list_data[start_index:end_index:step]


def list_copy(request, source_list):
    return source_list.copy()


def list_count(request, list_data):
    return len(list_data)


def list_index(request, list_data, indexing_item):
    return list_data.index(indexing_item)


def list_insert(request, list_data, item_to_be_inserted, index):
    list_data.insert(index, item_to_be_inserted)
    return list_data


def list_reverse(request, list_data):
    list_data.reverse()
    return list_data


def list_sort(request, list_data):
    list_data.sort()
    return list_data


def list_substraction(request, left_list1, right_list):
    list3 = list()
    for list_item in left_list1:
        if list_item not in right_list:
            list3.append(list_item)
    return list3


def list_remove(request, list_data, item_to_be_removed):
    list_data.remove(item_to_be_removed)
    return list_data


def clear(request, list_data):
    list_data.clear()
    return list_data





