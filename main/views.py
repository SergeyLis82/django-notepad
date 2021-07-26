from django.shortcuts import render

# Create your views here.

def index(request):
  data = {
    "title": "Main page",
    "values": ["Some", "Hello", "2021"],
    "obj": {"Car": "Schevrolet", "Hobby": "Sport", "Job": "DevOps"},
  }
  return render(request, 'main/index.html', data)

def about(request):
  return render(request, 'main/about.html')