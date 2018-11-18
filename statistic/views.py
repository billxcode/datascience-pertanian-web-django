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
    MATRIX = defineMatrix()
    SQR = kuadratElement(MATRIX)
    SUM = sumRow(SQR, MATRIX)
    PREFERENSI = preferensi(SUM)
    RATIO = priceQualityRatio(PREFERENSI)
    tanamans = Tanaman.objects.all()
    context = {
        'tanamans' : tanamans,
        'preferensi' : list(RATIO)
    }
    # return render(request, 'graph/json.html', { 'preferensi' : RATIO})
    return render(request, 'graph/result.html', context)

def defineMatrix():
    FULLMATRIX = []
    tanamans = Tanaman.objects.all()
    for t in tanamans:
        MATRIX = []
        for k in t.kriteria_set.all():
            MATRIX.append(int(k.value))
        FULLMATRIX.append(MATRIX)
    return FULLMATRIX


def kuadratElement(MATRIX):
    SQR = []
    for t in MATRIX:
        HELPER = []
        for k in t:
            HELPER.append(int(k)**2)
        SQR.append(HELPER)
    return SQR 

# ratio system
def sumRow(SQR, MATRIX):
    SUM = []
    panjang_baris = list(range(len(SQR[0])))
    panjang_kolom = list(range(len(SQR)))
    for s in panjang_baris:
        helper = 0
        for e in panjang_kolom:
            helper += SQR[e][s]
        helper = sqrt(helper)
        SUM.append(helper)
    
    INDEX = 0
    NORMAL = [] 
    for sq in list(range(len(MATRIX))):
        HELPER = []
        INDEX += 1
        for el in list(range(len(MATRIX[0]))):
            result = MATRIX[sq][el]/SUM[el]
            HELPER.append(result)
        NORMAL.append(HELPER)
   
    return NORMAL
 
def preferensi(NORMAL):
    PREFERENSI = []
    for terbobot in NORMAL:
        HELPER = 0
        MAIN_KRITERIA = 0
        INDEX = 0
        for el in terbobot:
            HELPER += el 
            if INDEX==0:
                MAIN_KRITERIA = el 
            INDEX +=1
        HASIL = HELPER-(MAIN_KRITERIA.real*2)
        PREFERENSI.append(HASIL.real)
    return PREFERENSI

def priceQualityRatio(PREFERENSI):
    kriterias = Kriteria.objects.filter(name_kriteria_id=4)
    index = 0
    HASIL = []
    for i in kriterias:
        helper = PREFERENSI[index]/float(i.value)
        index += 1
        HASIL.append(float(helper.real))
    return HASIL



        


