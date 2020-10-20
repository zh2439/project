from django.urls import path

from . import views

app_name='squirrel'

urlpatterns = [
        path('sightings/',views.index),
        path('sightings/add/',views.add,name='add'),

        path('sightings/<Unique_SquirrelID>/',views.update,name='update'),
        path('map/', views.map, name='map'),
]
