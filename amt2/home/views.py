from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Pessoa  

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'INDEX.html')

def cadastrar(request):
    if request.method == 'POST':

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        endereco = request.POST.get('endereco')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')


        Pessoa.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            cpf=cpf,
            data_nascimento=data_nascimento,
            endereco=endereco,
            cidade=cidade,
            estado=estado
        )
        return redirect('listar')

    return render(request, 'cadastrar.html')


def consultar(request):
    query = request.GET.get('q', '')
    pessoas = Pessoa.objects.filter(nome__icontains=query) if query else []
    return render(request, 'consultar.html', {'pessoas': pessoas, 'seu_nome': query})


def listar(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'listar.html', {'pessoas': pessoas})


def deletar(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('listar')
    return render(request, 'deletar.html', {'pessoa': pessoa})


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')
