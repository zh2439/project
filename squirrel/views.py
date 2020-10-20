from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Squirrel
from .forms import Update,Add

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
    }

    return render(request,'squirrel/index.html',context)

def add(request):
    if request.method == 'POST':
        form = Update(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")

    form=Update()
    context = {
            'form':form,
    }
    return render(request,'squirrel/add.html',context)

def update(request,Unique_SquirrelID):
    if request.method == 'POST':
        squirrel =get_object_or_404(Squirrel, Unique_SquirrelID=Unique_SquirrelID)
        form = Update(request.POST, instance=squirrel)
        if form.is_valid():
            squirrel.save()
            return redirect('/sightings/')
    squirrel =get_object_or_404(Squirrel, Unique_SquirrelID=Unique_SquirrelID)
    form = Update(instance=squirrel)
    context = {
            'form':form,
    }
    return render(request, 'squirrel/update.html', context)

