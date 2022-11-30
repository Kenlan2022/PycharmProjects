from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
    #查詢所有產品按name 序列
    queryset = Product.objects.all().order_by('name')
    #指定 序列化 類別
    serializer_class = ProductSerializer