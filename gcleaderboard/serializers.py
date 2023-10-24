from rest_framework import serializers
from bodies.models import Body
from gcleaderboard.models import GC, GC_Hostel_Points
from messmenu.models import Hostel
from messmenu.serializers import HostelSerializer

class GCSerializer(serializers.ModelSerializer):
    class Meta:
        model = GC
        fields = "__all__"


class TypeGCSerializer(serializers.ModelSerializer):

    hostels  = serializers.SerializerMethodField()
    gc = serializers.SerializerMethodField()

    def get_gc(self, obj):
        return GCSerializer(obj).data

    def get_hostels(self, obj):
        return [Hostel_Serializer(obj.hostel).data for obj in GC_Hostel_Points.objects.filter(gc=obj).order_by("-points")[:3]]

    class Meta:
        model = GC_Hostel_Points
        fields = ["gc", "hostels"]


class Hostel_PointsSerializer(serializers.ModelSerializer):

    hostel = serializers.SerializerMethodField()
    
    def get_hostel(self, obj):
        return HostelSerializer(obj.hostel).data

    class Meta:
        model = GC_Hostel_Points
        fields = ["hostel", "points"]


class Hostel_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hostel
        fields = "__all__"

class Body_Serializer(serializers.ModelSerializer):
    
    class Meta:
        model = Body
        fields = "__all__"

class Participants_Serializer(serializers.ModelSerializer):

    class Meta:
        model = GC_Hostel_Points
        fields = ["participants"]
