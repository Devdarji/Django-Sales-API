from django.db import models
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .searializers import *

# Create your views here.
def home(request):
    sales_data = Sale.objects.all()
    context = {
        'sales_data':sales_data
    }
    return render(request, 'home.html', context)


class SaleList(APIView):
    def get(self, request):
        model = Sale.objects.all()
        serializer =  SaleSerializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SaleSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SaleDetail(APIView):
    def get_sale(self, id):
        try:
            model = Sale.objects.get(id=id)
            print(model)
            return model
        except Sale.DoesNotExist:
            return Response(f'Sale {id} is Not Found in Database.', status=status.HTTP_404_NOT_FOUND)

    def get(self,request, id):
        if not self.get_sale(id):
            return Response(f"Sale with {id} is Not Found in Database.", status=status.HTTP_400_BAD_REQUEST)
        serializer = SaleSerializer(self.get_sale(id))
        return Response(serializer.data)

    def put(self,request, id):
        if not self.get_sale(id):
            return Response(f"Sale with {id} is Not Found in Database.", status=status.HTTP_400_BAD_REQUEST)
        serializer = SaleSerializer(self.get_sale(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        if not self.get_sale(id):
            return Response(f"Sale with {id} is Not Found in Database.", status=status.HTTP_400_BAD_REQUEST)
        model = self.get_sale(id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)