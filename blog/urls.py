from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), # '' means homepage, homepage route(views.home)
    path('about/', views.about, name='blog-about')
]
