from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import requests
from .constants import url, complete_address, key, api_key
import xml.etree.ElementTree as Et
from xml.dom import minidom


@api_view(['POST'])
def get_address_details(request):
    address = "+".join(request.data["address"].split(' '))
    output_format = request.data["output_format"]
    address_url = url + output_format + complete_address + address + key + api_key
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
        tree = Et.fromstring(response.text)
        formatted_address = tree.find("result").find("formatted_address").text
        lat = tree.find("result").find("geometry").find("location").find("lat").text
        lng = tree.find("result").find("geometry").find("location").find("lng").text
        root = Et.Element("root")
        Et.SubElement(root, "address").text = formatted_address
        coordinates = Et.SubElement(root, "coordinates")
        Et.SubElement(coordinates, "lat").text = lat
        Et.SubElement(coordinates, "lng", ).text = lng
        pretty = minidom.parseString(Et.tostring(root)).toprettyxml(indent="    ")
        return Response(pretty)
