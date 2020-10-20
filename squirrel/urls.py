from django.urls import path

from . import views

app_name='squirrel'

urlpatterns = [
        path('',views.index),
        path('<Unique_SquirrelID>/',views.update,name='update'),
]
