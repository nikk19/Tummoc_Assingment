from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DistanceSerializer
import math

@api_view(['POST'])
def calculate_distance(request):
    serializer = DistanceSerializer(data=request.data)
    if serializer.is_valid():
        lat1 = serializer.validated_data['lat1']
        lon1 = serializer.validated_data['lon1']
        lat2 = serializer.validated_data['lat2']
        lon2 = serializer.validated_data['lon2']

        distance = math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)

        return Response({'distance': distance})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)