from django.urls import path
from gcleaderboard.views import InstiViewSet, GCAdminViewSet, GCAdminPostViewSet

urlpatterns = [
   
    path(
        "typegc/<Type>/",
        InstiViewSet.as_view(
            {
                "get": "Type_GC",
            }
        ),
    ),

    path(
        "individualgclb/<pk>/",
        InstiViewSet.as_view(
            {
                "get": "Individual_GC_LB",
            }
        ),
    ),

    path(
        "typegclb/<Type>",
        InstiViewSet.as_view(
            {
                "get": "Type_GC_LB",
            }
        ),
    ),
    path(
        "overallgclb/",
        InstiViewSet.as_view(
            {
                "get": "GC_LB",
            }
        ),
    ),
    path(
        "postGC",
        GCAdminPostViewSet.as_view(
            {
                "post": "create",
            }
        ),
    ),
    path(
        "update_hostel_points/<pk>/",
        GCAdminViewSet.as_view(
            {
                "put": "update_points",
            }
        ),
    ),
    path(
        "get_available_hostels_bodies",
        GCAdminPostViewSet.as_view(
            {
                "get": "hostels_bodies",
            }
        ),
    ),

    # path(
    #     "participantsgc/<hostel_short_name>/<points_id>/",
    #     InstiViewSet.as_view(
    #         {
    #             "get": "Participants_in_GC",
    #         }
    #     ),
    # ),

]
############################################################################
# path('', views.apiOverview,  name = "Api - Overview"),
# path('get/', views.getData,  name = "Article - Get"),
# path('add/',views.addArticle,name = "Article - Add"),
# path('update/<str:pk>/',views.UpdateArticle ,  name = "Article - Update"),
# path('delete/<str:pk>/',views.DeleteArticle ,  name = "Article - Delete"),

##########################################################################
""" 
path('types', views.Types_Of_GCs ,  name = "Types Of GC"),
path('cult', views.Cult_GC ,  name = "Cult GC"),
path('tech', views.Tech_GC ,  name = "Tech GC"),
path('sports', views.Sports_GC ,  name = "Sports GC"),
path('subgclb/<str:gc_ID>/', views.Sub_GC_LB),

path('typegclb/<str:type>/', views.Type_GC_LB),
path('gclb/', views.GC_LB),
path('post_GC/', views.add_GC),
path('update_score/', views.update_Points),

]
"""
