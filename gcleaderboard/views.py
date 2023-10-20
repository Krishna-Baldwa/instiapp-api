from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from rest_framework import viewsets
from .models import GC, GC_Hostel_Points, Hostel
from messmenu.serializers import HostelSerializer
from roles.helpers import user_has_privilege
from roles.helpers import login_required_ajax

from rest_framework.response import Response
from .serializers import (
    GCSerializer,
    Hostel_PointsSerializer,
    Hostel_Serializer,
    
)

from gcleaderboard.serializers import Participants_Serializer 

def get_GC(gc_id):
    """
    Helper function to get GC object by ID. Returns None if not found.
    """
    return get_object_or_404(GC, id=gc_id)

class InstiViewSet(viewsets.ModelViewSet):
    queryset = GC.objects
    serializer_class = GCSerializer
  
   

    def Type_GC(
        self,
        request,
        Type,
    ):
        """  List of GCs of a particular Type """
        gcs = GC.objects.filter(type=Type)
        serializer = GCSerializer(gcs, many=True)
        return Response(serializer.data)


    def Individual_GC_LB(self, request, gc_id):
        
        """ List Of Hostels sorted w.r.t points for leaderboard of that gc """
        gc = get_GC(gc_id)
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
    
    def Participants_in_GC(self ,  request , points_id ,hostel_short_name ):
         participants = GC_Hostel_Points.objects.filter(
                hostel__short_name=hostel_short_name, id = points_id
            )
         
         serializer = Participants_Serializer(participants , many = True)
         return Response(serializer.data)
         




class GCAdminViewSet(viewsets.ModelViewSet):
    queryset = GC.objects.all()
    serializer_class = GCSerializer

    @login_required_ajax
    def add_GC(self, request):
        """ Adding New GC """
        if user_has_privilege(request.user.profile, 'GCAdmin'):
            participating_hostels_data = request.data.get('participating_hostels', [])
            serializer = GCSerializer(data=request.data)
            if serializer.is_valid():
                gc = serializer.save()

                gc.participating_hostels.set(participating_hostels_data)
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        return Response({"detail": "You do not have the required permissions to add GCs."}, status=403)


class GCAdminViewSet(viewsets.ModelViewSet):
    queryset = GC_Hostel_Points.objects.all()  # Replace with your queryset
    serializer_class = Hostel_Serializer

    @login_required_ajax
    def update_points(self, request, pk):
        """ Modify Hostel Points for a GC """
        if user_has_privilege(request.user.profile, 'GCAdmin'):
            gc_hostel_points = get_object_or_404(GC_Hostel_Points, id=pk)    
            change_point = int(request.data.get("points", 0))
            gc_hostel_points.points += change_point
            gc_hostel_points.save()
            return Response({"message": "Points updated"})
