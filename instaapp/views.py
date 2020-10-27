from django.shortcuts import render,redirect
from .forms import RegisterForm,ImageForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Image, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/signin/')
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
        
    return render(request, 'register.html', {'form': form})

@login_required(login_url='/signin/')
def search_profile(request):
    if 'search_user' in request.GET and request.GET["search_user"]:
        search_term = request.GET.get("search_user")
        result_image = Image.search_user(search_term)
        message = f"{search_term}"
        
        return render(request, 'home.html',{"images": result_image, "message":message})

    else:
        return redirect('home')

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

@login_required(login_url='/signin/')
def my_profile(request):
    current_user = request.user
    images = Image.objects.filter(user=current_user.id)

    if request.method=='POST':
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            image = Image()
            image.caption = request.POST.get('caption')
            image.user = current_user
            image.name = request.FILES['image']
            image.image = request.FILES['image']
            image.save()
      
            return redirect('profile')
    else:
        form = ImageForm()
    return render(request, 'profile.html', {'form': form, 'images': images})

@login_required(login_url='/signin/')
def like(request, image_id):
    image = Image.objects.get(id=image_id)
    image.likes = image.likes + 1
    image.save()
    images = Image.objects.all()
    
    return render(request, 'home.html', {'images':images})

@login_required(login_url='/signin/')
def comment(request, image_id):
    image = Image.objects.get(id=image_id)

    if request.method == 'POST':
        
        Comment.objects.create(
            image=image,
            user=request.user,
            comment=request.POST.get('comment')
        )

    comments = Comment.objects.filter(image=image.id)
    
    return render(request, 'image_comments.html', {'image':image, 'comments': comments})

@login_required(login_url='/signin/')
def signout(request):
    logout(request)
    return redirect('signin')