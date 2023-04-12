from django.shortcuts import render
from rest_framework.views import APIView
from herbal.models import Herbal
from herbal.serializer import HerbalSerializer
from rest_framework.response import Response

# Create your views here.

class herbal_list(APIView):
    def get(self,request):
        herbals = Herbal.objects.all()
        serializer= HerbalSerializer(herbals,many = True)
        return Response(serializer.data)
    
class HerbalCreate(APIView):
    def post(self,request):
        serializer = HerbalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)