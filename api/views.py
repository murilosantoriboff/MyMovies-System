from django.shortcuts import render
from .serializers import FilmeSerializer
from movies.models import Filme
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getfilme(request):
    filmes = Filme.objects.all()
    serializer = FilmeSerializer(filmes, many=True)
    return Response(serializer.data)