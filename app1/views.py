from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
#from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from .serializers import SmartphoneSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Smartphone

@api_view(['GET'])
def AllSmartphones(request):
    obj = Smartphone.objects.all()
    serializer = SmartphoneSerializer(data=obj, many=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
@api_view(['GET','PUT','PATCH','DELETE','POST'])
def DetailPhone(request, pk):
    if request.method == 'GET':
        obj = Smartphone.objects.get(pk=pk)
        ser = SmartphoneSerializer(obj)
        return Response(ser.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        obj=Smartphone.objects.get(pk=pk)
        ser=SmartphoneSerializer(instance=obj,data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        obj=Smartphone.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/api')
    elif request.method=='POST':
        ser = SmartphoneSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def Personroot(request):
    info={'person':'info'}
    d=dict(request.GET)
    for i in d:
        d[i]=d[i][0]
    info.update(d)
    return Response(info)
class Getall(ModelViewSet):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer

import requests
def URLshorten(request):

    val = request.POST.get('url_val')


    url = "https://url-shortener-service.p.rapidapi.com/shorten"

    payload = {"url": val}
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "6048b1f9f0msh6393f3aeec90d8dp1dce27jsn6c0a696ccd4a",
        "X-RapidAPI-Host": "url-shortener-service.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    res = response.json()

    return render(request, 'service.html', {'result': res})












# # Create your views here.
# class SmartphonePage(ListAPIView):
#     queryset = Smartphone.objects.all()
#     def get(self,request,*args,**kwargs):
#         allsmartphone= Smartphone.objects.all().order_by('year')
#         serializer= SmartphoneSerializer(allsmartphone, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
# class SmartphoneCreate(CreateAPIView):
#     queryset = Smartphone.objects.all()
#     serializer_class = SmartphoneSerializer


# class SmartPhoneRUD(RetrieveUpdateDestroyAPIView):
#     queryset = Smartphone.objects.all()
#     serializer_class = SmartphoneSerializer





