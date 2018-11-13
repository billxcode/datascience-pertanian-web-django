# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from MOORA.models import Kriteria, Bobot, Tanaman

# Create your views here.

def index(request):
    return render(request, 'graph/result.html')

def procesData(request):
    kriteria = Kriteria.objects.all()
    return HttpResponse(kriteria)