from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from Productos.models import *
from Productos.serializador import *


def pagina(request):
    return HttpResponse('Aquí se construye un sueño fresco y verde')


class apipersonal (viewsets.ModelViewSet):
    serializer_class = Serialpersonal
    queryset = Productos.objects.all()
