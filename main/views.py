from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import *
import time
from django.shortcuts import render
from django.http import HttpResponse
import subprocess
# Create your views here.

def homepage(request):
    return render(request, 'template.html')

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

def testWithoutIndex(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    datum_kreiranja = request.GET.get('datum_kreiranja', '')
    
    url = f"http://localhost:8000/withoutIndex/?naziv={naziv}&cijena={cijena}&datum_kreiranja={datum_kreiranja}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena,
            'datum_kreiranja': datum_kreiranja,
        },
        'output': output,
    }
    
    return JsonResponse(response_data)

def testWithIndex(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    datum_kreiranja = request.GET.get('datum_kreiranja', '')
    
    url = f"http://localhost:8000/withIndex/?naziv={naziv}&cijena={cijena}&datum_kreiranja={datum_kreiranja}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena,
            'datum_kreiranja': datum_kreiranja,
        },
        'output': output,
    }
    
    return JsonResponse(response_data)

def testWithPartIndex(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    datum_kreiranja = request.GET.get('datum_kreiranja', '')
    
    url = f"http://localhost:8000/withPartIndex/?naziv={naziv}&cijena={cijena}&datum_kreiranja={datum_kreiranja}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena,
            'datum_kreiranja': datum_kreiranja,
        },
        'output': output,
    }
    
    return JsonResponse(response_data)

def testWithWrongIndex(request):
    naziv = request.GET.get('naziv', '')
    cijena = request.GET.get('cijena', '')
    datum_kreiranja = request.GET.get('datum_kreiranja', '')
    
    url = f"http://localhost:8000/withWrongIndex/?naziv={naziv}&cijena={cijena}&datum_kreiranja={datum_kreiranja}"
    result = subprocess.run(['ab', '-n', '1000', '-c', '3', url], capture_output=True, text=True)
    output = result.stdout.splitlines()
    
    response_data = {
        'parameters': {
            'naziv': naziv,
            'cijena': cijena,
            'datum_kreiranja': datum_kreiranja,
        },
        'output': output,
    }
    
    return JsonResponse(response_data)