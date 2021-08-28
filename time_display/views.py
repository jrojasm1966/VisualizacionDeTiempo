from django.http import HttpResponse
from django.shortcuts import render
from time import gmtime, strftime, localtime
from datetime import datetime

# Create your views here.
def root(request):
    return HttpResponse("Mi Inicio: Directorio root")

def index(request):
    
    context = {
        "time0": datetime.now().strftime("%Y-%m-%d %H:%M %p"),
        "time1": strftime("Fecha: %a %d - Mes %b - Año %Y --- Hora: %Y %H:%M %p", localtime()),
        "time2": strftime("Fecha: Dia %d - Mes %m - Año %Y --- Hora: %Y %H:%M %p", localtime()),
        "time3": strftime("Fecha: %a %d - Mes %b - Año %Y --- Hora: %Y %H:%M %p", gmtime()),
        "time4": strftime("Fecha: Dia %d - Mes %m - Año %Y --- Hora: %Y %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)
