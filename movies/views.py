from django.shortcuts import render
from django.http import HttpResponse
from .models import Filme
from django.shortcuts import get_object_or_404, redirect

def home(request):
    filmes = Filme.objects.all()
    return render(request, 'home.html', {'filmes':filmes})

def ver_detalhes(request, id):
    filme = get_object_or_404(Filme, pk=id)
    return render(request, 'ver_detalhes.html', {'filme':filme})

def atualizar_filme(request):
    if request.method == 'POST':
        id_filme = request.POST.get('id_filme')
        nome = request.POST.get('nome_filme')
        sinopse = request.POST.get('sinopse_filme')
        diretor = request.POST.get('diretor_filme')
        ano_lancamento = request.POST.get('ano_lancamento_filme')

        filme_velho = Filme.objects.get(id=id_filme)

        novo_filme = Filme(nome=nome, sinopse=sinopse, diretor=diretor, ano_lancamento=ano_lancamento)

        novo_filme.save()

        filme_velho.delete()

        return redirect('/movies/home/?status=updated')

def excluir_filme(request, id):
    filme = Filme.objects.get(id=id)
    return render(request, 'excluir_filme.html', {'filme':filme})

def confirmar_exclusao(request, id):
    filme = Filme.objects.get(id=id)
    filme.delete()
    return redirect('/movies/home/?deleted=true')

def criar_filme(request):
    return render(request, 'criar_filme.html')

def validacao_criacao_filme(request):
    if request.method == 'POST':
        nome_filme = request.POST.get('nome_filme')
        diretor_filme = request.POST.get('diretor_filme')
        ano_lancamento_filme = request.POST.get('ano_lancamento_filme')
        sinopse = request.POST.get('sinopse_filme')

        novo_filme = Filme(nome=nome_filme, sinopse=sinopse, diretor=diretor_filme, ano_lancamento=ano_lancamento_filme)

        novo_filme.save()

        return redirect('/movies/home/?created_movie=success')
    else:
        return redirect('/movies/home/?verification_form=false')