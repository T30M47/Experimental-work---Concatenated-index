from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import *
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse('<h1>Testing read request response time with and without concatenated index.</h1>')

class GetDataWithoutIndex(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        datum_kreiranja = request.GET.get('datum_kreiranja', '')

        proizvodi = Proizvod_bezIndeksa.objects.filter(
            naziv = naziv,
            cijena = cijena,
            datum_kreiranja = datum_kreiranja
        )

        proizvodi_json = list(proizvodi.values())
        return JsonResponse(proizvodi_json, safe=False)

class GetDataWithIndex(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        datum_kreiranja = request.GET.get('datum_kreiranja', '')

        proizvodi = Proizvod_SIndeksom.objects.filter(
            naziv = naziv,
            cijena = cijena,
            datum_kreiranja = datum_kreiranja
        )

        proizvodi_json = list(proizvodi.values())
        return JsonResponse(proizvodi_json, safe=False)

class GetDataWithPartIndex(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        datum_kreiranja = request.GET.get('datum_kreiranja', '')

        proizvodi = Proizvod_DioIndeksa.objects.filter(
            naziv = naziv,
            cijena = cijena,
            datum_kreiranja = datum_kreiranja
        )

        proizvodi_json = list(proizvodi.values())
        return JsonResponse(proizvodi_json, safe=False)

class GetDataWithWrongIndex(View):
    def get(self, request):
        naziv = request.GET.get('naziv', '')
        cijena = request.GET.get('cijena', '')
        datum_kreiranja = request.GET.get('datum_kreiranja', '')

        proizvodi = Proizvod_KriviIndeks.objects.filter(
            naziv = naziv,
            cijena = cijena,
            datum_kreiranja = datum_kreiranja
        )

        proizvodi_json = list(proizvodi.values())
        return JsonResponse(proizvodi_json, safe=False)