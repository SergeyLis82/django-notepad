from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.db import IntegrityError
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

def signupuser(request):
  data = {
    "title": "SignUp",
    "heading": "Регистрация нового пользователя",
    "content": "",
    "error": "",
    "form": UserCreationForm(),
  }
  if request.method == "GET":
    return render(request, 'main/signupuser.html', data)
  else:
    if request.POST['password1'] == request.POST['password2']:
      try:
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
        user.save()
        login(request, user)
        return redirect('main:home')
      except IntegrityError:
        data["error"] = "Пользователь с указанным именем уже существует. Введите другое имя пользователя."
        return render(request, 'main/signupuser.html', data)
    else:
      data["error"] = "Введёные пароли не совпадают"
      return render(request, 'main/signupuser.html', data)

def loginuser(request):
  data = {
    "title": "Login",
    "heading": "Форма входа пользователя пользователя",
    "content": "",
    "error": "",
    "form": AuthenticationForm(),
  }
  if request.method == "GET":
    return render(request, 'main/loginuser.html', data)
  else:
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is None:
      data['error'] = "Пользователь или пароль не найдены"
      return render(request, 'main/loginuser.html', data)
    else:
      login(request, user)
      return redirect('main:home')

    

def logoutuser(request):
  if request.method == "POST":
    logout(request)
    return redirect('main:home')