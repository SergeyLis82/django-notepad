from django.shortcuts import render

# Create your views here.

def index(request):
  data = {
    "title": "Привет!",
    "says": "Никто не стремится получать советы, зато деньги получать горазды все;\nвыходит - деньги лучше, чем советы.\n		-- Дж.Свифт"
  }
  return render(request, 'main/index.html', data)

def about(request):
  return render(request, 'main/about.html')