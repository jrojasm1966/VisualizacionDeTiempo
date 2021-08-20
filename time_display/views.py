from django.http import HttpResponse
from django.shortcuts import render
from time import gmtime, strftime, localtime

# Create your views here.
def root(request):
    return HttpResponse("Mi Inicio: Directorio root")

def index(request):
    
    #Probar con un for en index.html
    #context = {
    #    "time" [ 
    #            strftime("Fecha: %a %d - Mes %b - Año %Y --- Hora: %Y %H:%M %p", gmtime()),
    #           strftime("Fecha: Dia %d - Mes %m - Año %Y --- Hora: %Y %H:%M %p", gmtime()),
    #            strftime("Fecha: %a %d - Mes %b - Año %Y --- Hora: %Y %H:%M %p", localtime()),
    #            strftime("Fecha: Dia %d - Mes %m - Año %Y --- Hora: %Y %H:%M %p", localtime())
    #    ]
    #}
    
    context = {
        "time1": strftime("Fecha: %a %d - Mes %b - Año %Y --- Hora: %Y %H:%M %p", gmtime()),
        "time2": strftime("Fecha: Dia %d - Mes %m - Año %Y --- Hora: %Y %H:%M %p", gmtime()),
        "time3": strftime("Fecha: %a %d - Mes %b - Año %Y --- Hora: %Y %H:%M %p", localtime()),
        "time4": strftime("Fecha: Dia %d - Mes %m - Año %Y --- Hora: %Y %H:%M %p", localtime())
    }
    return render(request,'index.html', context)
