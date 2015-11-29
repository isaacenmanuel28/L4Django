from django.shortcuts import render

from django.http import HttpResponse
from .models import Country
#from Countries.forms import CountryForm
#from Countries.forms import CityForm
#from Countries.forms import LanguageForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from django.shortcuts import render_to_response


def home(request):
    Paises = Country.objects.all()[:10]
    return render_to_response('index.html', {'paises' : Paises})


def index(request):
    return HttpResponse("Tarea T4 Programacion 2.")

#def crear(request):
   # if request.POST:
  #      form = CountryForm(request.POST)
 #       if form.is_valid():
#            form.save()

     #       return HttpResponseRedirect('/')
    #else:
     #   form = CountryForm()

    #args = {}
    #args.update(csrf(request))

    #args['form'] = form

   # return render_to_response('crear_country.html', args)