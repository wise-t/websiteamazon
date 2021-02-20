from django.urls import path ,re_path
from . import views
app_name='affiliate'
urlpatterns = [
    path('',views.home, name='index'),
    path('about',views.about, name='about'),
    path('contact',views.home, name='contact'),
    path('services',views.home, name='services'),
    path('ex',views.home, name='ex'),
    
]