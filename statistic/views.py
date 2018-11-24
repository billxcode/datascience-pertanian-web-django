# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import serializers
from django.http import HttpResponse, JsonResponse
from MOORA.models import Kriteria, Bobot, Tanaman, NameKriteria, Preferensi, RatioQuality
from cmath import sqrt
from decimal import Decimal

# Create your views here.

def index(request):
    TANAMAN_ID = 0
    TANAMAN_USER = 0
    if 'pupuk' in request.GET:
        TANAMAN_USER = [float(request.GET['pupuk']), float(request.GET['lahan']), float(request.GET['suhu'])]
        TANAMAN_ID = int(request.GET['tanaman'])
    MATRIX = defineMatrix(TANAMAN_USER)
    SQR = kuadratElement(MATRIX)
    SUM = sumRow(SQR, MATRIX)
    PREFERENSI = preferensi(SUM)
    # return render(request, 'graph/json.html', {'preferensi': PREFERENSI})
    RATIO = priceQualityRatio(PREFERENSI, TANAMAN_ID)
    pref = Preferensi.objects.order_by('-value').all()
    tanamans = Tanaman.objects.all()
    context = {
        'tanamans' : list(tanamans), 
        'preferensi' : list(pref)
    }
    return render(request, 'graph/result.html', context)

# create matrix from all data
def defineMatrix(TANAMAN_USER):
    FULLMATRIX = []
    tanamans = Tanaman.objects.all()
    for t in tanamans:
        MATRIX = []
        for k in t.kriteria_set.all():
            MATRIX.append(int(k.value))
        FULLMATRIX.append(MATRIX)
    if TANAMAN_USER!=0:
        FULLMATRIX.append(TANAMAN_USER)
    return FULLMATRIX

# sqr all element
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

# calculate preferensi 
def preferensi(NORMAL):
    PREFERENSI = []
    for terbobot in NORMAL:
        HELPER = 0
        MAIN_KRITERIA = 0
        INDEX = 0
        for el in terbobot:
            HELPER += el 
            if INDEX==2:
                MAIN_KRITERIA = el 
            INDEX +=1
        HASIL = HELPER-(MAIN_KRITERIA.real*2)
        PREFERENSI.append(HASIL.real)
    return PREFERENSI


# price quality ratio by hasil panen
def priceQualityRatio(PREFERENSI, TANAMAN_ID):
    ratio = RatioQuality.objects.all()
    if TANAMAN_ID!=0:
        ratio_user = RatioQuality.objects.get(tanaman=TANAMAN_ID)
    tanamans = Tanaman.objects.all()
    Preferensi.objects.all().delete()
    index = 0
    HASIL = []
    jumlah_array_preferensi = len(PREFERENSI)
    for i in range(jumlah_array_preferensi):
        pref = Preferensi()
        helper = 0
        if TANAMAN_ID!=0:
            if i==(jumlah_array_preferensi-1):
                helper = PREFERENSI[i]/float(ratio_user.value)
                pref.tanaman_id = TANAMAN_ID
            else:
                helper = PREFERENSI[i]/float(ratio[i].value)
                pref.tanaman_id = tanamans[index].id
        else:
           helper = PREFERENSI[i]/float(ratio[i].value)
           pref.tanaman_id = tanamans[index].id
        pref.value = round(Decimal(helper), 7)
        pref.save()
        index += 1
        HASIL.append(pref.value)
    return HASIL



