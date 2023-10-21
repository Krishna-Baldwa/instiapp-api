from rest_framework import serializers
from gcleaderboard.models import GC, GC_Hostel_Points
from messmenu.serializers import HostelSerializer

class GCSerializer(serializers.ModelSerializer):
    class Meta:
        model = GC
        fields = "__all__"


class TypeGCSerializer(serializers.ModelSerializer):

    hostels  = serializers.SerializerMethodField()
    gc = serializers.SerializerMethodField()

    def get_gc(self, obj):
        return obj.name

    def get_hostels(self, obj):
        return [obj.hostel.name for obj in GC_Hostel_Points.objects.filter(gc=obj).order_by("-points")[:3]]

    class Meta:
        model = GC_Hostel_Points
        fields = ["gc", "hostels"]


class Hostel_PointsSerializer(serializers.ModelSerializer):

    hostel_name = serializers.SerializerMethodField()

    def get_hostel_name(self, obj):
        return obj.hostel.name

    class Meta:
        model = GC_Hostel_Points
        fields = ["hostel_name", "points"]


class Hostel_Serializer(serializers.ModelSerializer):
    class Meta:
        model = GC_Hostel_Points
        fields = ["points"]

class Participants_Serializer(serializers.ModelSerializer):

    class Meta:
        model = GC_Hostel_Points
        fields = ["participants"]
