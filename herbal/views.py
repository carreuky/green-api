from rest_framework.views import APIView
from herbal.models import Herbal
from herbal.serializer import HerbalSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class herbal_list(APIView):
    def get(self,request):
        herbals = Herbal.objects.all()
        serializer= HerbalSerializer(herbals,many = True)
        return Response(serializer.data)
    
class herbal_create(APIView):
    def post(self,request):
        serializer = HerbalSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        Response(serializer.data)

class herbal_each(APIView):
    def get_herbal_by_id(self,pk):
        try:
           return Herbal.objects.get(pk=pk)
        except:
            return Response({
                'error':'Herbal does not exist'
            },status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        herbal=self.get_herbal_by_id(pk)
        serializer=HerbalSerializer(herbal)
        return Response(serializer.data)
    def put(self,request,pk):
        herbal=self.get_herbal_by_id(pk)
        serializer=HerbalSerializer(herbal,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        herbal = self.get_herbal_by_id(pk)
        herbal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

