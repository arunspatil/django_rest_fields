# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import (
    Operations
)
from .constants import (
    new_name_success_message,
    name_delete_error_message,
    empty,
    name_delete_success_message,
    new_name_error_message,
    name_does_not_exists
)
# Create your views here.


@api_view(['GET'])
def get_all_operations(request):
    all_data = [each_operation.name for each_operation in Operations.objects.all()]
    return Response({'objects': all_data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_operation(request):
    new_name = request.data['new_name']
    if new_name and new_name != empty:
        Operations.objects.create(name=new_name)
        return Response({'message': new_name_success_message}, status=status.HTTP_200_OK)
    else:
        return Response({'error': new_name_error_message})


@api_view(['POST'])
def delete_operation(request):
    new_name = request.data['new_name']
    if new_name and new_name != empty:
        exist = True if Operations.objects.filter(name=new_name) else False
        if exist:
            Operations.objects.filter(name=new_name).delete()
            return Response({'message': name_delete_success_message}, status=status.HTTP_200_OK)
        else:
            return Response({'error': name_does_not_exists})
    else:
        return Response({'error': name_delete_error_message})
