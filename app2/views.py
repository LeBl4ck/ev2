from django.shortcuts import render

# Create your views here.

def meme2(request):
    data ={
        "Categoria":"gatito",
        "Imagen": "/static/gatito_lloron.jpg",
        "Comentario": "cuando te va mal en el certamen",
    }
    return render(request, 'index.html', data)

def meme1 (request):
    data ={
        "Categoria":"perro mamado",
        "Imagen": "/static/perro_mamado.jpg",
        "Comentario": "cuando aprendes a programar / cuando te falla el codigo",
    }
    return render(request, 'index.html', data)

def meme3 (request):
    data ={
        "Categoria":"capybara",
        "Imagen": "/static/capybara.jpg",
        "Comentario": "cuando el profeso te aprueba igual",
    }
    return render(request, 'index.html', data)