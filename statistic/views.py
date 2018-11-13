# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from MOORA.models import Kriteria, Bobot, Tanaman, NameKriteria
from cmath import sqrt

# Create your views here.

JUMLAH = 0

def index(request):
    BOBOT = []
    SQR = kuadratElement()
    SUM = sumRow(SQR)
    NORMAL = normalization(SQR, SUM)
    NORMAL_TERBOBOT = normalizationTerbobot(BOBOT, NORMAL)
    PREFERENSI = preferensi(NORMAL_TERBOBOT)
    return render(request, 'graph/result.html', {'preferensi':PREFERENSI})

def kuadratElement():
    tanamans = Tanaman.objects.all()
    SQR = []
    for t in tanamans:
        HELPER = []
        for k in t.kriteria_set.all():
            HELPER.append(int(k.value)**2)
        SQR.append(HELPER)
    return SQR

def sumRow(SQR):
    SUM = []
    for s in SQR:
        helper = 0
        for e in s:
            helper += e 
        SUM.append(helper)
    return SUM

def normalization(SQR, SUM):
    INDEX = 0
    NORMAL = [] 
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
    return NORMAL 

def normalizationTerbobot(BOBOT, NORMAL):
    NORMAL_TERBOBOT = []
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
    return NORMAL_TERBOBOT
        
def preferensi(NORMAL_TERBOBOT):
    PREFERENSI = []
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
    return PREFERENSI

        


