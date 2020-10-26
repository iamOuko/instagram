from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('search/', views.search_profile, name = 'search_profile'),
    path('signin/', views.signin, name = 'signin'),
    path('profile/', views.my_profile, name = 'profile'),
    
  
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)