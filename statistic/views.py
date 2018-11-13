# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from MOORA.models import Kriteria, Bobot, Tanaman, NameKriteria

# Create your views here.

SQR = []
HELPER = []
SUM = []

def index(request):
    return render(request, 'graph/result.html')

def kuadratElement(request):
    kriterias = Kriteria.objects.all()
    tanamans = Tanaman.objects.all()
    for t in tanamans:
        for k in t.kriteria_set.all():
            HELPER.append(int(k.value)**2)
        SQR.append(HELPER)

def sumRow(request):
    for s in SQR:
        helper = 0
        for e in s:
            helper += e 
        SUM.append(helper)

