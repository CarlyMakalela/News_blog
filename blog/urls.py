from django.urls import path
from . import views
from . views import about

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),     
    path('contact/', views.contact, name='contact'),  

]
