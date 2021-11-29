from django.shortcuts import render

# Create your views here.

def index(request):
  data = {
    "title": "Home",
    "heading": "Привет!",
    "content": "Никто не стремится получать советы, зато деньги получать горазды все;\nвыходит - деньги лучше, чем советы.\n		-- Дж.Свифт"
  }
  return render(request, 'main/index.html', data)

def about(request):
  data = {
    "title": "About",
    "heading": "About page",
    "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus sit voluptatum, praesentium, corrupti illo aliquam blanditiis officiis incidunt obcaecati nisi assumenda. Praesentium doloribus eos commodi reiciendis culpa animi ut et"
  }
  return render(request, 'main/about.html', data)