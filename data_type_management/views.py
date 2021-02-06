# from django.shortcuts import render
from .models import Operations
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .constants import invalid, create_success_message, create_failure_message, delete_failure_message,\
    delete_success_message, empty_message, keyError


@api_view(['GET'])
def get_all_operations(request):
    objects_list = [[each_object.name, each_object.id] for each_object in Operations.objects.all()]
    return Response({"Data": objects_list}, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_operations(request):
    try:
        new_name = request.data['new_name']
        if new_name not in invalid:
            name = Operations.objects.create(name=new_name)
            if name:
                return Response({"Message": create_success_message}, status=status.HTTP_200_OK)
            else:
                return Response({"error": create_failure_message}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Error": empty_message}, status=status.HTTP_400_BAD_REQUEST)
    except KeyError:
        return Response({"Error": keyError})


@api_view(['POST'])
def delete_operations(request):
    try:
        object_name = request.data['new_name']
        if object_name not in invalid:
            name = Operations.objects.filter(name=object_name)
            if name:
                Operations.objects.filter(name=object_name).delete()
                return Response({"message": object_name + delete_success_message})
            else:
                return Response({"Error": delete_failure_message}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Error": empty_message}, status=status.HTTP_400_BAD_REQUEST)
    except KeyError:
        return Response({"Error": keyError})


@api_view(['POST'])
def delete_all_operations(request):
    Operations.objects.all().delete()
    return Response({"message": "successfully removed"})



