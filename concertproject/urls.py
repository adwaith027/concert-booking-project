
from django.contrib import admin
from django.urls import path
from concertapp import views

urlpatterns = [
    path('signup/', views.signup,name='signup'),
    path('login/', views.userlogin,name='login'),
    path('logout/', views.userlogout,name='logout'),
    path('createconcert/', views.createconcert,name='createconcert'),
    path('bookconcert/', views.bookconcert,name='bookconcert'),
]