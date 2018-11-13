# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from MOORA.models import Kriteria, Bobot, Tanaman, NameKriteria
from cmath import sqrt

# Create your views here.

SQR = []
SUM = []
NORMAL = []
NORMAL_TERBOBOT = []
BOBOT = []
PREFERENSI = []

def index(request):
    if kuadratElement()==True:
        if sumRow()==True:
            if normalization()==True:
                if normalizationTerbobot()==True:
                    if preferensi()==True:
                        context = {
                            'preferensi' : PREFERENSI
                        }
                        return render(request, 'graph/result.html', context) 
    return HttpResponse("failed")

def kuadratElement():
    kriterias = Kriteria.objects.all()
    tanamans = Tanaman.objects.all()
    for t in tanamans:
        HELPER = []
        for k in t.kriteria_set.all():
            HELPER.append(int(k.value)**2)
        SQR.append(HELPER)
    return True

def sumRow():
    for s in SQR:
        helper = 0
        for e in s:
            helper += e 
        SUM.append(helper)
    return True

def normalization():
    INDEX = 0 
    for sq in SQR:
        HELPER = []
        for el in sq:
            resultElement = int(SUM[INDEX])-int(el)
            sqrtSqr = sqrt(el)
            sqrtElement = sqrt(resultElement)
            result = sqrtSqr/sqrtElement
            HELPER.append(result)
        NORMAL.append(HELPER)
        INDEX += 1
    return True

def normalizationTerbobot():
    bobots = Bobot.objects.all()
    for bobot in bobots:
        BOBOT.append(bobot.value)
    for nor in NORMAL:
        HELPER = []
        INDEX = 0
        for el in nor:
            result = float(BOBOT[INDEX].real)*float(el.real)
            HELPER.append(result) 
            INDEX += 1
        NORMAL_TERBOBOT.append(HELPER)
    return True
        
def preferensi():
    for terbobot in NORMAL_TERBOBOT:
        HELPER = 0
        MAIN_KRITERIA = 0
        INDEX = 0
        for el in terbobot:
            HELPER += el 
            if INDEX==1:
                MAIN_KRITERIA = el 
            INDEX +=1
        PREFERENSI.append(HELPER-(MAIN_KRITERIA*2))
    return True

        


