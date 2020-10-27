from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('search/', views.search_profile, name = 'search_profile'),
    path('signin/', views.signin, name = 'signin'),
    path('signout/', views.signout, name = 'signout'),
    path('profile/', views.my_profile, name = 'profile'),
    path('like/<int:image_id>', views.like, name = 'like'),
    path('comment/<int:image_id>', views.comment, name = 'comment'),
  
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)