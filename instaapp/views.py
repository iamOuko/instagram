from django.shortcuts import render,redirect
from .forms import RegisterForm,ImageForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Image

# Create your views here.
def welcome(request):
    current_user = request.user
    images = Image.objects.all()
    
    return render(request, 'home.html', {'images':images})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('welcome')
    else:
        form = RegisterForm()
        print(form)
    return render(request, 'register.html', {'form': form})

def search_profile(request):
    if 'search_user' in request.GET and request.GET["search_user"]:
        search_term = request.GET.get("search_user")
        result_profile = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message})

    else:
        message = "Enter search item!"
        return render(request, 'search.html', {"message":message})

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form}) 

def my_profile(request):
    id = request.user.id
    images = Image.objects.filter(user=id)

    if request.method=='POST':
        form = ImageForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            image = Image()
            image.caption = request.POST.get('caption')
            image.user = id
            image.save()
      
            return redirect('my_profile')
    else:
        form = ImageForm()
        
    return render(request, 'profile.html', {'form': form, 'images': images})


