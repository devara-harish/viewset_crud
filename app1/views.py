from django.shortcuts import render
from rest_framework.response import Response
from app1.serializers import *
from app1.models import *
from rest_framework.viewsets import ViewSet

# Create your views here.
class ProductCrudvs(ViewSet):
    def list(self,request):
        PQS=Product.objects.all()
        PSD=productserializers(PQS,many=True)
        return Response(PSD.data)
    

    def retrieve(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPS=productserializers(SPO)
        return Response(SPS.data)
    
    def create(self,request):
        SD=productserializers(data=request.data)
        if SD.is_valid():
            SD.save()
            return Response({'success':'product is created'})
        else:
            return Response({'failed':'product is not created'})
        

    def update(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=productserializers(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'success':'product is updated'})
        else:
            return Response({'failed':'product is not updated'})
        


    def partial_update(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=productserializers(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'success':'product is partially_updated'})
        else:
            return Response({'failed':'product is not partially_updated'})
        



    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'deleted':'product is deleted'})
    
        






