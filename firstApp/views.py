from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from firstApp.models import Countries
from firstApp.serializers import CountriesSerializer
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET','POST'])
def countries_list(request):
    if request.method == 'GET':
        countries = Countries.objects.all() #get all countries

        name = request.GET.get('name', None)
        if name is not None:
            countries = countries.filter(name_icontains = name) #filter countries only with certain letters if u want
        countries_serializer = CountriesSerializer(countries,many=True) #getting from model so change to JSON for output
        return JsonResponse(countries_serializer.data, safe = False)


    elif request.method == 'POST':
        countries_data = JSONParser().parse(request) #JSON to Python
        countries_serializer = CountriesSerializer(data = countries_data) #Python to Model/SQL
        if countries_serializer.is_valid(): #Check if fields are correct like India, New Delhi valid
            countries_serializer.save() #create new row
            return JsonResponse(countries_serializer.data,status = status.HTTP_201_CREATED)
        return JsonResponse(countries_serializer.data,status = status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET','PUT','DELETE']) #pk is column id number
def countries_detail(request,pk):
    try:
        countries = Countries.objects.get(pk=pk) #access pk-th element in database
    except Countries.DoesNotExist:
        return JsonResponse({'message': 'The country does not exist'} , status = status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        countries_serializer = CountriesSerializer(countries) # Individual element in Model to JSON
        return JsonResponse(countries_serializer.data)
    
    elif request.method == 'PUT':
        countries_data = JSONParser().parse(request) #JSON to Python
        countries_serializer = CountriesSerializer(countries, data = countries_data) #Create new object
        if countries_serializer.is_valid():
            countries_serializer.save() #append to database
            return JsonResponse(countries_serializer.data) #return element u added
        return JsonResponse(countries_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        countries.delete()
        return JsonResponse({'message:' 'Country Deleted Successfully!'}, status = status.HTTP_204_NO_CONTENT)
