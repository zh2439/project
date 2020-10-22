from django.urls import path

from . import views

app_name='squirrel'

urlpatterns = [
        path('',views.home,name='home'),
        path('sightings/',views.index),
        path('sightings/add/',views.add,name='add'),
        path('map/', views.map, name='map'),
        path('sightings/stats/',views.stats, name='stats'),
        path('sightings/<Unique_SquirrelID>/',views.update,name='update'),
]
