# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from MOORA.models import Kriteria, Bobot, Tanaman, NameKriteria

# Create your views here.

SQR = []
SUM = []
NORMAL = []
NORMAL_TERBOBOT = []
BOBOT = []

def index(request):
    return render(request, 'graph/result.html')

def kuadratElement(request):
    kriterias = Kriteria.objects.all()
    tanamans = Tanaman.objects.all()
    for t in tanamans:
        HELPER = []
        for k in t.kriteria_set.all():
            HELPER.append(int(k.value)**2)
        SQR.append(HELPER)
    return True

def sumRow(request):
    for s in SQR:
        helper = 0
        for e in s:
            helper += e 
        SUM.append(helper)
    return True

def normalization(request):
    for sm in SUM:
        HELPER = []
        for sq in SQR:
            resultElement = int(sm)-int(sq)
            sqrtSqr = sqrt(sq)
            sqrtElement = sqrt(resultElement)
            result = sqrtSqr/sqrtElement
            HELPER.append(result)
        NORMAL.append(HELPER)
    return True

def normalizationTerbobot(request):
    bobots = Bobot.objects.all()
    for bobot in bobots:
        BOBOT.append(bobot.value)
    for nor in NORMAL:
        HELPER = []
        INDEX = 0
        for el in nor:
            result = BOBOT[INDEX]*el
            HELPER.append(result) 
            INDEX += 1
        NORMAL_TERBOBOT.append(HELPER)
    return True
        


        


