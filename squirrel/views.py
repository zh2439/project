from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from .models import Squirrel

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
    }

    return render(request,'squirrel/index.html',context)
