from django.shortcuts import render
from .models import Property
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
#imports services web
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PropertySerializer
#AJAX
from django.urls import reverse_lazy, reverse


def index(request):
    return render(request, 'home.html')

# Properties List
class PropertyList(ListView):
    model = Property

    def get_queryset(self):
        queryset = Property.objects.filter(available=True)
        return queryset

#Property Detail
class PropertyDetail(DetailView):
    model = Property

def searchProperty(request):
    if request.method == 'POST':
        pattern = request.POST['search']
        property = Property.objects.filter(available=True, neighborhood__contains=pattern)
    else:
        property = Property.objects.filter(available=True)
    return render(request, 'property/property_search.html', {'object_list':property, 'search':pattern})


#Web Service Rest
class PropertyAPI(APIView):
    #show all properties
    def get(self, request):
        property = Property.objects.all()
        serializer = PropertySerializer(property, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        property = PropertySerializer.objects.get(pk=pk)
        serializer = PropertySerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        property = Property.objects.get(pk=pk)
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Create property
class PropertyCreate(CreateView):
    model = Property
    success_url = reverse_lazy('property:create')
    fields = '__all__'


    #Property_management
    class Propertymanagement(CreateView):
        model = Property
        success_url = reverse_lazy('')
        fields = '__all__'

#Informatión Pagina Property
def hello(request):
        return render(request, 'hello.html')
