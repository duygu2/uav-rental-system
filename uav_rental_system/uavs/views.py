from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Uavs, Brand, Category
from .serializers import UavsSerializer, BrandSerializer, CategorySerializer

def home(request):
    return render(request,"index.html")

@csrf_exempt
def uav_list(request):
    request.method=='GET'
    uavs= Uavs.objects.all()
    uavs_serializer=UavsSerializer(uavs,many=True)
    return JsonResponse(uavs_serializer.data,safe=False)

@csrf_exempt
def uav_list_by_id(request, id):
    try:
        uav = Uavs.objects.get(id=id)
    except Uavs.DoesNotExist:
        return JsonResponse({'message': 'UAV not found'})

    uav_serializer = UavsSerializer(uav)
    return JsonResponse(uav_serializer.data)

@csrf_exempt
def uav_create(request):
    if request.method == 'POST':
        uav_data = JSONParser().parse(request)
        uav_serializer = UavsSerializer(data=uav_data)

        if uav_serializer.is_valid():
            category_id = uav_data.get('category')
            brand_id = uav_data.get('brand')

            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                return JsonResponse({'message': 'Invalid category'}, status=400)

            try:
                brand = Brand.objects.get(id=brand_id)
            except Brand.DoesNotExist:
                return JsonResponse({'message': 'Invalid brand'}, status=400)

            uav_serializer.save()
            return JsonResponse(uav_serializer.data, status=201)

        return JsonResponse(uav_serializer.errors, status=400)
    return JsonResponse({'message': 'Invalid request method'}, status=405)

@csrf_exempt
def uav_update(request, id):
    try:
        uav = Uavs.objects.get(id=id)
    except Uavs.DoesNotExist:
        return JsonResponse({'message': 'UAV not found'})

    if request.method == 'PUT':
        uav_data = JSONParser().parse(request)
        uav_serializer = UavsSerializer(uav, data=uav_data)
        if uav_serializer.is_valid():
            uav_serializer.save()
            return JsonResponse(uav_serializer.data)
        return JsonResponse(uav_serializer.errors)
    return JsonResponse({'message': 'Invalid method'})

@csrf_exempt
def uav_delete(request, id):
    try:
        uav = Uavs.objects.get(id=id)
    except Uavs.DoesNotExist:
        return JsonResponse({'message': 'UAV not found'})

    uav.delete()
    return JsonResponse({'message': 'UAV deleted successfully'})



@csrf_exempt
def brand_list(request):
    request.method=='GET'
    brands= Brand.objects.all()
    brands_serializer=BrandSerializer(brands,many=True)
    return JsonResponse(brands_serializer.data,safe=False)

@csrf_exempt
def brand_add(request):
    request.method=='POST'
    brand_data=JSONParser().parse(request)
    brand_serializer=BrandSerializer(data=brand_data)
    if brand_serializer.is_valid():
        brand_serializer.save()
        return JsonResponse("Added ASuccessfully", safe=False)
    return JsonResponse("Failed to Add",safe=False)

@csrf_exempt
def brand_update(request,id):
    request.method=='PUT'
    brand_data=JSONParser().parse(request)
    brand= Brand.objects.get(id=brand_data["id"])
    brand_serializer=BrandSerializer(brand, data=brand_data)
    if brand_serializer.is_valid():
        brand_serializer.save()
        return JsonResponse("Update Successfully",safe=False)
    return JsonResponse("Failed to Update",safe=False)

@csrf_exempt
def brand_delete(request,id):
    request.method=='DELETE'
    brand=Brand.objects.get(id=id)
    brand.delete()
    return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        categories_serializer = CategorySerializer(categories, many=True)
        return JsonResponse(categories_serializer.data, safe=False)

@csrf_exempt
def category_add(request):
    if request.method == 'POST':
        category_data = JSONParser().parse(request)
        category_serializer = CategorySerializer(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

@csrf_exempt
def category_update(request, id):
    if request.method == 'PUT':
        category_data = JSONParser().parse(request)
        category = Category.objects.get(id=id)
        category_serializer = CategorySerializer(category, data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

@csrf_exempt
def category_delete(request, id):
    if request.method == 'DELETE':
        category = Category.objects.get(id=id)
        category.delete()
        return JsonResponse("Deleted Successfully", safe=False)

