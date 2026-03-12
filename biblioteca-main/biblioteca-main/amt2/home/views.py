from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro


def home(request):
    return render(request, 'home.html')


def cadastrar(request):

    if request.method == 'POST':

        titulo = request.POST.get('titulo')
        autor = request.POST.get('autor')
        editora = request.POST.get('editora')
        ano = request.POST.get('ano')
        paginas = request.POST.get('paginas')
        categoria = request.POST.get('categoria')
        isbn = request.POST.get('isbn')
        idioma = request.POST.get('idioma')
        descricao = request.POST.get('descricao')
        cadastrado_por = request.POST.get('cadastrado_por')

        Livro.objects.create(
            titulo=titulo,
            autor=autor,
            editora=editora,
            ano=ano,
            paginas=paginas,
            categoria=categoria,
            isbn=isbn,
            idioma=idioma,
            descricao=descricao,
            cadastrado_por=cadastrado_por
        )

        return redirect('listar')

    return render(request, 'cadastrar.html')


def consultar(request):

    query = request.GET.get('q')

    livros = []

    if query:
        livros = Livro.objects.filter(titulo__icontains=query)

    return render(request, 'consultar.html', {'livros': livros})


def listar(request):

    livros = Livro.objects.all()

    return render(request, 'listar.html', {'livros': livros})


def deletar(request, id):

    livro = get_object_or_404(Livro, id=id)

    if request.method == 'POST':
        livro.delete()
        return redirect('listar')

    return render(request, 'deletar.html', {'livro': livro})


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')