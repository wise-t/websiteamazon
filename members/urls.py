from django.urls import path, include
from .views import UserRegisterViews
#rom.import views
app_name='members'
urlpatterns = [
    path('register/',UserRegisterViews.as_view(),name='register'),
    path('oauth/', include('social_django.urls', namespace='social')),

]