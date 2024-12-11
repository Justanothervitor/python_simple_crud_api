from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from webapp.models import Product
from webapp.serializers import ProductInfoSerializer


# Create your views here.

@api_view(['GET'])
def get_products_list(request):
    products = Product.objects.all()    
    products_serializer = ProductInfoSerializer(products,many=True)
    return JsonResponse(products_serializer.data,safe=False)

@api_view(['GET'])
def get_single_product(request,pk):
    requested_product = Product.objects.get(pk=pk)
    print(requested_product)
    product_serializer = ProductInfoSerializer(requested_product)
    if product_serializer is not None:
        return JsonResponse(product_serializer.data,safe=True,status=status.HTTP_302_FOUND)
    return JsonResponse("Nao foi possivel encontrar o produto!",safe=False,status=status.HTTP_404_NOT_FOUND)    


@api_view(['POST'])
def post_product(request):
    request_info = JSONParser().parse(request)
    product_serializer = ProductInfoSerializer(data=request_info)
    if product_serializer.is_valid():
        product_serializer.save()
        return JsonResponse("Produto criado com sucesso!",safe=False,status=status.HTTP_201_CREATED)
    print(product_serializer.errors)
    return JsonResponse("Nao foi possivel criar o produto!",safe=False,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def get_and_update_product(request,pk):
    try:
        to_update_info = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse("Produto nao encontrado!",safe=False,status=status.HTTP_404_NOT_FOUND)
    updateInfo = JSONParser().parse(request)

    product_updater_serializer = ProductInfoSerializer(to_update_info,data=updateInfo)
    if product_updater_serializer.is_valid():
        product_updater_serializer.save()
        return JsonResponse("As informacoes do produto foram atualizadas!",safe=False,status=status.HTTP_200_OK)
    print(product_updater_serializer.errors)    
    return JsonResponse("Nao foi possivel atualizar as informacoes do produto!",safe=False,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_a_product(request,pk):
    try:
        to_delete_info = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse("Nao eh possivel apagar um produto inexistente!",safe=False,status=status.HTTP_404_NOT_FOUND)
    
    to_delete_info.delete()
    return JsonResponse("O produto requisitado foi apagado com sucesso!",safe=False,status=status.HTTP_204_NO_CONTENT)
        