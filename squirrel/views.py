from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .models import Squirrel
from .forms import Update,Add

def home(request):

    return render(request,'squirrel/home.html',{})

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels':squirrels,
    }

    return render(request,'squirrel/index.html',context)


def add(request):
    if request.method == 'POST':
        form = Add(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/sightings/")

    form=Add()
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

def map(request):
    squirrels = Squirrel.objects.all()
    sq_list = []
    for sq in squirrels:
        if len(sq_list)<100:
            sq_list.append({'latitude':sq.Latitude,'longitude':sq.Longitude})
    context = {
            'sightings':sq_list,
    }
    return render(request,'squirrel/map.html',context)

def stats(request):
    total_sightings = Squirrel.objects.all().count()
    total_running = Squirrel.objects.filter(Running=True).count()
    total_chasing = Squirrel.objects.filter(Chasing=True).count()
    total_eating = Squirrel.objects.filter(Eating=True).count()
    total_climbing = Squirrel.objects.filter(Climbing=True).count()
    total_foraging = Squirrel.objects.filter(Foraging=True).count()
    total_morning = Squirrel.objects.filter(Shift='AM').count()
    total_afternoon = Squirrel.objects.filter(Shift = 'PM').count()
    total_adults = Squirrel.objects.filter(Age='Adult').count()
    total_juveniles = Squirrel.objects.filter(Age='Juvenile').count()
    total_gray = Squirrel.objects.filter(Primary_Color='Gray').count()
    total_cinnamon = Squirrel.objects.filter(Primary_Color='Cinnamon').count()
    total_black = Squirrel.objects.filter(Primary_Color='Black').count()
    context = {
            'total_sightings': total_sightings,
            'total_running': total_running,
            'total_chasing': total_chasing,
            'total_eating': total_eating,
            'total_climbing': total_climbing,
            'total_foraging': total_foraging,
            'total_morning': total_morning,
            'total_afternoon': total_afternoon,
            'total_adults': total_adults,
            'total_juveniles': total_juveniles,
            'total_gray': total_gray,
            'total_cinnamon': total_cinnamon,
            'total_black': total_black,
    }
    return render (request,'squirrel/stats.html',context)



