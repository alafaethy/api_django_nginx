from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


def home(request):
    
    return HttpResponse('<h1> TELA INICIAL </h1>')

def api_views(request):
    
    return HttpResponse('<h1> CRIADO UM API PARA UTILIZAR COM NGINX </h1>')


@api_view(['GET'])
def hellow(request):
    
    return Response({'msg': 'CRIADO UM API PARA UTILIZAR COM NGINX'})