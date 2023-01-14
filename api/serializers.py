from movies.models import Filme
from rest_framework import serializers

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['nome', 'sinopse', 'diretor', 'ano_lancamento']