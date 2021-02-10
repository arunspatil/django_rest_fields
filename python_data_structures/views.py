from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .list import *
from .constants import *

# Create your views here.


@api_view(['GET'])
def list_append_view(request):
    try:
        list1 = request.data['list1'].split()
        number = request.data['number']
    except KeyError:
        return Response({"error": something_went_wrong})
    if is_list(list1):
        return Response({"list": list_append(list1, number)}, status=status.HTTP_200_OK)
    else:
        return Response({'error': something_went_wrong}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_extend_view(request):
    try:
        list1 = request.data['list1'].split()
        list2 = request.data['list2'].split()
    except KeyError:
        return Response({"error": something_went_wrong})
    # list1 = create_list()
    # list2 = create_list()
    if is_list(list1) and is_iterable(list2):
        return Response({"list": list_extend(list1, list2)}, status=status.HTTP_200_OK)
    else:
        return Response({'error': something_went_wrong}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_slicing_view(request):
    default_start_index, default_step, default_end_index = 0, 1, 0
    list_data = []
    try:
        list_data = request.data['list1'].split()
        if list_data:
            end_index = int(request.data['end_index'])
    except KeyError:
        end_index = len(list_data)
    try:
        start_index = int(request.data['start_index'])
    except KeyError:
        start_index = default_start_index
    try:
        step = int(request.data['step'])
    except KeyError:
        step = default_step
    finally:
        if is_list(list_data):
            if type(start_index) is int and type(step) is int and type(end_index) is int:
                if step < 0 and end_index == len(list_data):
                    end_index = default_end_index
                    start_index = len(list_data)
                return Response({'list': list_slicing(list_data, start_index, end_index, step)}, status=status.HTTP_200_OK)
            else:
                return Response({'error': something_went_wrong}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': something_went_wrong}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_copy_view(request):
    try:
        source_list = request.data['source_list'].split()
    except KeyError:
        return Response({"error": something_went_wrong})
    if is_list(source_list):
        return Response({"list": list_copy(source_list)}, status=status.HTTP_200_OK)
    else:
        return Response({'error': something_went_wrong}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_count_view(request):
    try:
        source_list = request.data['source_list'].split()
    except KeyError:
        return Response({"error": something_went_wrong})
    if is_list(source_list):
        return Response({"list": list_count(source_list)}, status=status.HTTP_200_OK)
    else:
        return Response({'error': something_went_wrong}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_index_view(request):
    try:
        source_list = request.data['source_list'].split()
        indexing_item = request.data['indexing_item']
    except KeyError:
        return Response({"error": something_went_wrong})
    if is_list(source_list):
        return Response({"index": list_index(source_list, indexing_item)}, status=status.HTTP_200_OK)
    else:
        return Response({'error': something_went_wrong}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_insert_view(request):
    try:
        list_data = request.data['list_data'].split()
        index = int(request.data['index'])
        item_to_be_inserted = request.data['item_to_be_inserted']
    except KeyError:
        return Response({"msg": something_went_wrong})
    if is_list(list_data) and type(index) is int:
        return Response({"list": list_insert(list_data, index, item_to_be_inserted)}, status=status.HTTP_200_OK)
    else:
        return Response({'error': something_went_wrong}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_reverse_view(request):
    try:
        list_data = request.data['list_data'].split()
    except KeyError:
        return Response({"error": something_went_wrong})
    if is_list(list_data):
        return Response({"list": list_reverse(list_data)}, status=status.HTTP_200_OK)
    else:
        return Response({'error': something_went_wrong}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_sort_view(request):
    try:
        list_data = request.data['list_data'].split()
    except KeyError:
        return Response({"error": something_went_wrong})
    if is_list(list_data):
        return Response({"list": list_sort(list_data)}, status=status.HTTP_200_OK)
    else:
        return Response({'error': something_went_wrong}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_substraction_view(request):
    list3 = list()
    try:
        left_list1 = request.data['left_list1'].split()
        right_list = request.data['left_list2'].split()
    except KeyError:
        return Response({"error": something_went_wrong})
    return Response({"list": list_substraction(left_list1, right_list)}, status=status.HTTP_200_OK)


@api_view(['GET'])
def list_remove_view(request):
    try:
        list_data = request.data['list_data'].split()
        item_to_be_removed = request.data['item_to_be_removed']
    except KeyError:
        return Response({"error": something_went_wrong})
    if is_list(list_data):
        return Response({"list": list_remove(list_data, item_to_be_removed)}, status=status.HTTP_200_OK)
    else:
        return Response({'error': something_went_wrong}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_clear_view(request):
    try:
        list_data = request.data['list_data'].split()
    except KeyError:
        return Response({"error": something_went_wrong})
    if is_list(list_data):
        return Response({"list": list_clear()}, status=status.HTTP_200_OK)
    else:
        return Response({'error': something_went_wrong}, status=status.HTTP_400_BAD_REQUEST)





