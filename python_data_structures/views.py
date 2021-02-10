from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .list import *
from .constants import *

# Create your views here.


@api_view(['POST'])
def list_append_view(request):
    list1 = request.data['list1']
    # number = input("Enter item to be appended to the list")
    number = request.data['number']
    Response({"list": list_append(list1, number)}, status=status.HTTP_200_OK)


@api_view(['POST'])
def list_extend_view(request):
    list1 = request.data['list1']
    list2 = request.data['list2']
    # list1 = create_list()
    # list2 = create_list()
    Response({"list": list_extend(list1, list2)}, status=status.HTTP_200_OK)


@api_view(['GET'])
def list_slicing_view(request):
    try:
        list_data = request.data['list1']
        start_index = request.data['start_index']
        end_index = request.data['end_index']
    except KeyError:
        return Response({"error": something_went_wrong})
    try:
        step = request.data['step']
    finally:
        if type(start_index) is int_type and type(end_index) is int_type:
            if type(step) is int_type:
                Response({'list': list_slicing(list_data, start_index, end_index, step)}, status=status.HTTP_200_OK)
        else:
            Response({'error': something_went_wrong}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def list_copy(request, source_list):
    return source_list.copy()


@api_view(['POST'])
def list_count(request, list_data):
    return len(list_data)


@api_view(['POST'])
def list_index(request, list_data, indexing_item):
    return list_data.index(indexing_item)


@api_view(['POST'])
def list_insert(request, list_data, item_to_be_inserted, index):
    list_data.insert(index, item_to_be_inserted)
    return list_data


@api_view(['POST'])
def list_reverse(request, list_data):
    list_data.reverse()
    return list_data


@api_view(['POST'])
def list_sort(request, list_data):
    list_data.sort()
    return list_data


@api_view(['POST'])
def list_substraction(request, left_list1, right_list):
    list3 = list()
    for list_item in left_list1:
        if list_item not in right_list:
            list3.append(list_item)
    return list3


@api_view(['POST'])
def list_remove(request, list_data, item_to_be_removed):
    list_data.remove(item_to_be_removed)
    return list_data


@api_view(['POST'])
def clear(request, list_data):
    list_data.clear()
    return list_data





