from django.shortcuts import render

# Create your views here.

def elec(request):
    data ={
        "Categoria":"Electronica",
        "Imagen": "/static/elec.png",
        "Comentario": "Tomorroland",
    }
    return render(request, 'index.html', data)

def pop (request):
    data ={
        "Categoria":"Pop",
        "Imagen": "/static/pop.png",
        "Comentario": "Denise Rosenthal",
    }
    return render(request, 'index.html', data)

def jazz (request):
    data ={
        "Categoria":"Jazz",
        "Imagen": "/static/jazz.png",
        "Comentario": "Jazz",
    }
    return render(request, 'index.html', data)