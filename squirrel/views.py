from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Squirrel
from .forms import Update

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
    }

    return render(request,'squirrel/index.html',context)

def update(request,Unique_SquirrelID):
    if request.method == 'POST':
        squirrel = get_object_or_404(Squirrel, Unique_SquirrelID=Unique_SquirrelID)
        form = Update(request.POST, instance=squirrel)
        if form.is_valid():
            sighting.save()
            return redirect('/sightings/')

    squirrel = get_object_or_404(Squirrel, Unique_SquirrelID=Unique_SquirrelID)
    form = Update(instance=squirrel)
    context = {
            'form':form,
    }
    return render(request, 'squirrel/update.html', context)

def
