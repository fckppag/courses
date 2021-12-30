from django.urls import path
from . import views

urlpatterns = [
    path('main', views.index, name='main'),
    path('', views.enter, name='home'),
    #path('register', views.register, name='reg'),
    #path('log_in', views.log_in, name='log'),
    #path('courses', views.course, name='course'),
    #path('stats', views.stats, name='stats'),
]
