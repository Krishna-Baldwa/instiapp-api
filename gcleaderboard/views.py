from django.shortcuts import render
from uuid import UUID
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from rest_framework import viewsets
from .models import GC, GC_Hostel_Points, Hostel
from messmenu.serializers import HostelSerializer
from roles.helpers import user_has_privilege
from roles.helpers import login_required_ajax
from roles.helpers import forbidden_no_privileges, insufficient_parameters
from rest_framework.response import Response
from .serializers import (
    GCSerializer,
    Hostel_PointsSerializer,
    Hostel_Serializer,
    TypeGCSerializer,
    
)

from gcleaderboard.serializers import Participants_Serializer 

def get_GC(self, pk):
        """Get an event from pk uuid or strid."""
        try:
            UUID(pk, version=4)
            return get_object_or_404(self.queryset, id=pk)
        except ValueError:
            return get_object_or_404(self.queryset, str_id=pk)
        
def get_GC_Hostel(self, pk):
        """Get an event from pk uuid or strid."""
        try:
            UUID(pk, version=4)
            return get_object_or_404(self.queryset, id=pk)
        except ValueError:
            return get_object_or_404(self.queryset, str_id=pk)

class InstiViewSet(viewsets.ModelViewSet):
    queryset = GC.objects
    serializer_class = GCSerializer

    def Type_GC(self,request,Type,):
        """GET list of GCs for a particular type.
        As in list of all tech GCs, Cult GCs, etc.
        This also has the first three rankers for every GC shown."""

        gcs = GC.objects.filter(type=Type)
        serializer = GCSerializer(gcs, many=True)
        return Response(serializer.data)


    def Individual_GC_LB(self, request, pk):
        """GET list of hostels for a particular GC ranked according to points."""

        gc = GC.objects.get(id=pk)
        gc_hostel_points = GC_Hostel_Points.objects.filter(gc=gc).order_by("-points")
        serializer = Hostel_PointsSerializer(gc_hostel_points, many=True)
        return Response(serializer.data)

    

    def Type_GC_LB(self, request, Type):
        """ Leaderboard for list of hostels for types of GC """
        data = []
        all_rows = Hostel.objects.all()
        for row in all_rows:
            # Access fields of the row
            curr_hostel_id = row.id
            curr_hostel_name = row.name

            Total_Points_Curr_Hostel = GC_Hostel_Points.objects.filter(
                hostel__id=curr_hostel_id, gc__type=Type
            ).aggregate(Total_Points=Coalesce(Sum("points"), Value(0)))["Total_Points"]

            data.append({
                "hostels": HostelSerializer(row).data,
                "points": Total_Points_Curr_Hostel
            })

        sorted_dict = sorted(data, key=lambda item: item["points"], reverse=True)
        print(sorted_dict)
        return Response(sorted_dict)


    def GC_LB(self, request):
        
        """ List of Hostels for Overall Leaderboard """
        data = []
        all_rows = Hostel.objects.all()
        for row in all_rows:
            curr_hostel_id = row.id

            Total_Points_Curr_Hostel = GC_Hostel_Points.objects.filter(
                hostel__id=curr_hostel_id
            ).aggregate(Total_Points=Coalesce(Sum("points"), Value(0)))["Total_Points"]

            data.append({
                "hostels": HostelSerializer(row).data,
                "points": Total_Points_Curr_Hostel
            })

        sorted_dict = sorted(data, key=lambda item: item["points"], reverse=True)

        print(sorted_dict)
        return Response(sorted_dict)
    
         

class GCAdminPostViewSet(viewsets.ModelViewSet):
    queryset = GC.objects.all()
    serializer_class = GCSerializer


    @login_required_ajax
    def create(self, request):
        """ POST a new GC. 
        Needs `AddGC` permission for each body to be associated.
        This also creates new entries for GC_Hostel_Points for each hostel."""

        # Prevent events without any body
        if 'body' not in request.data or not request.data['body']:
            return insufficient_parameters()
    
        if user_has_privilege(request.user.profile, request.data['body'], 'GCAdm'):
            gc = super().create(request)
            participating_hostel = request.data.getlist('participating_hostels')
            for hostel in participating_hostel:
                GC_Hostel_Points.objects.create(
                    gc=GC.objects.get(id=gc.data['id']),
                    hostel=Hostel.objects.get(id=hostel),
                    points=0,
                )
            return gc
        return forbidden_no_privileges()


class GCAdminViewSet(viewsets.ModelViewSet):
    queryset = GC_Hostel_Points.objects.all()  # Replace with your queryset
    serializer_class = Hostel_Serializer

    @login_required_ajax
    def update_points(self, request, pk):
        """ Update points for a hostel in a GC.
        Needs `GCAdm` permission for the body of the GC."""

        gc = GC_Hostel_Points.objects.get(id=pk).gc

        if user_has_privilege(request.user.profile, gc.body.id, 'GCAdm'):
            gc_hostel_points = GC_Hostel_Points.objects.get(id=pk)
            change_point = int(request.data.get("points", 0))
            gc_hostel_points.points += change_point
            gc_hostel_points.save()
            return Response({"message": "Points updated"})
