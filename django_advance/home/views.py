from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    names = ["Ram", "Mohan", "Abhijeet", "Anjali"]
    items = {
        "pen": 5,
        "pencil": 10,
        "eraser": 6
    }
    context = {
        "names" : names,
        "items": items
    }
    return render(request, 'index.html', context)


def contact(request):
    return render (request, 'contact.html')

def about(request):
    return render (request, 'about.html')

def dynamic_route(request, number):
    for i in range(0,10):
        print(f"{number} * {i} = {number * i}")
        
    return HttpResponse(f"Responce by Dynamic route {number}")

