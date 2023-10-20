from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def meme2(request):
    data ={
        "Categoria":"gatito",
        "Imagen": "static/gatito_lloron.jpeg",
        "Comentario": "cuando te va mal en el certamen",
        
    }
    return render(request, 'index.html', data)

def meme1 (request):
    data ={
        "Categoria":"perro mamado",
        "imagen":'static/perro_mamado.jpeg',
        "Comentario" : "cuando aprendes a programar / cuando te falla el codigo",
        
    }
    return render(request, 'index.html', data)

def meme3 (request):
    data ={
        "Categoria":"capybara",
        "Imagen": "static/capybara.jpeg",
        "Comentario": "cuando el profeso te aprueba igual",
        
    }
    return render(request, 'index.html', data)