from django.shortcuts import render
import subprocess
# Create your views here.

def index(request):
  output = subprocess.getoutput('fortune')
  data = {
    "title": "Home",
    "heading": "Привет!",
    "content": output
  }
  return render(request, 'main/index.html', data)

def about(request):
  data = {
    "title": "About",
    "heading": "About page",
    "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus sit voluptatum, praesentium, corrupti illo aliquam blanditiis officiis incidunt obcaecati nisi assumenda. Praesentium doloribus eos commodi reiciendis culpa animi ut et"
  }
  return render(request, 'main/about.html', data)