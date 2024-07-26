from rest_framework import serializers

class DistanceSerializer(serializers.Serializer):
    lat1 = serializers.FloatField()
    lon1 = serializers.FloatField()
    lat2 = serializers.FloatField()
    lon2 = serializers.FloatField()