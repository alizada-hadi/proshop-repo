from django.shortcuts import render
from rest_framework import serializers
from rest_framework import response
from rest_framework.decorators import api_view
from ..models import Product
from rest_framework.response import Response
from ..serializers import ProductSerializers


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializers(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializers(product, many=False)
    return Response(serializer.data)
