from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('course/', views.course, name='course'),
    path('erwhh/', views.stats, name='stats'),
    path('course/<int:course_id>/', views.subcourse, name='subs')
]

