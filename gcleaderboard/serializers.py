from rest_framework import serializers
from gcleaderboard.models import GC, GC_Hostel_Points
from messmenu.serializers import HostelSerializer

class GCSerializer(serializers.ModelSerializer):
    participating_hostels = HostelSerializer(many=True, read_only=True)
    class Meta:
        model = GC
        fields = "__all__"


class Hostel_PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GC_Hostel_Points
        fields = ["hostel", "points"]


class Hostel_Serializer(serializers.ModelSerializer):
    class Meta:
        model = GC_Hostel_Points
        fields = ["points"]

class Participants_Serializer(serializers.ModelSerializer):

    class Meta:
        model = GC_Hostel_Points
        fields = ["participants"]
