from django.shortcuts import render
import subprocess
# Create your views here.

def index(request):
  output = subprocess.getoutput('fortune')
  data = {
    "title": "Home",
    "heading": "Привет!",
    #"content": output
    "content": """Великий Мастер бился с Хаосом. И чем крепче он бился, тем больше к нему приходило мыслей. Когда приходили мысли о толковом, он записывал их, предваряя магическим словом TODO:. Мысли же о бестолковом он тоже записывал, но для таких мыслей у него было другое магическое слово — FIXME:. И надо сказать, что от Начала Времён для победы над Хаосом не было более сильных заклинаний, чем эти два."""
  }
  return render(request, 'main/index.html', data)

def about(request):
  data = {
    "title": "About",
    "heading": "About page",
    "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus sit voluptatum, praesentium, corrupti illo aliquam blanditiis officiis incidunt obcaecati nisi assumenda. Praesentium doloribus eos commodi reiciendis culpa animi ut et"
  }
  return render(request, 'main/about.html', data)