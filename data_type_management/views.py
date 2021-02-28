from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import xml.etree.ElementTree as ET
from xml.dom import minidom

from .models import Operations
from .constants import (
    invalid_strings,
    create_success_message,
    delete_failure_message,
    delete_success_message,
    name_not_valid,
    something_went_wrong
)


@api_view(['GET'])
def get_all_operations(request):
    objects_list = [[each_object.name, each_object.id] for each_object in Operations.objects.all()]
    return Response({"data": objects_list}, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_operation(request):
    try:
        new_name = request.data['new_name']
    except KeyError:
        return Response({"error": something_went_wrong})
    if new_name not in invalid_strings:
        Operations.objects.create(name=new_name)
        return Response({"message": create_success_message}, status=status.HTTP_201_CREATED)
    else:
        return Response({"error": name_not_valid}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def delete_operation(request):
    # try:
    #     object_name = request.data['new_name']
    # except KeyError:
    #     return Response({"error": something_went_wrong})
    # if object_name not in invalid_strings:
    #     name = Operations.objects.filter(name=object_name)
    #     if name:
    #         Operations.objects.filter(name=object_name).delete()
    #         return Response({"message": object_name + delete_success_message})
    #     else:
    #         return Response({"error": object_name + delete_failure_message},
    #                         status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return Response({"error": name_not_valid}, status=status.HTTP_400_BAD_REQUEST)
    address = request.data["address"]
    address = "+".join(address.split(' '))
    output_format = request.data["output_format"]
    api_key = 'AIzaSyCOD3KvY2DDzEfel-NZ_LKIWXr86EF_EUw'
    address_url = "https://maps.googleapis.com/maps/api/geocode/" + output_format + "?address=" + address + "&key=" + \
                  api_key
    response = requests.get(address_url)
    if output_format == 'json':
        formatted_address = response.json()['results'][1]['formatted_address']
        coordinates = response.json()['results'][1]['geometry']['location']
        return Response(
            {
                "coordinates": coordinates,
                "address": formatted_address
            }, status=status.HTTP_200_OK)
    elif output_format == 'xml':
        # tree = ET.parse(response.text)
        # print(tree)
        # root = tree.getroot()
        tree = ET.fromstring(response.text)
        formatted_address = tree.find("result").find("formatted_address").text
        lat = tree.find("result").find("geometry").find("location").find("lat").text
        lng = tree.find("result").find("geometry").find("location").find("lng").text
        root = ET.Element("root")
        print(formatted_address)
        ET.SubElement(root, "address").text = formatted_address
        coordinates = ET.SubElement(root, "coordinates")
        ET.SubElement(coordinates, "lat").text = lat
        ET.SubElement(coordinates, "lng",).text = lng
        pretty = minidom.parseString(ET.tostring(root)).toprettyxml(indent="    ")
        print(pretty)
        return Response(pretty)


@api_view(['POST'])
def delete_all_operations(request):
    Operations.objects.all().delete()
    return Response({"message": "successfully removed"})


# lsof -nP -iTCP -sTCP:LISTEN | grep 8000 # list active ports pid in MAC

