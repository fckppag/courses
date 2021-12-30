from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course
from .forms import CourseForm
import random



def index(request):
	users = Course.objects.all()
	return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks':users})


def enter(request):
	return render(request, 'main/enter.html')


'''def register(request):
	error = ''
	if request.method == 'POST':
		form = CourseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'Incorrect form'

	form = CourseForm()
	context={
		'form': form,
		'error': error
	}
	return render(request, 'main/register.html', context)


def log_in(request):
	error = ''
	form = CourseForm()
	if request.method == 'GET':
		form = CourseForm(request.GET)
		if ==Course.ID_Pass:
			return redirect('home')
		else:
			error = 'Incorrect form'
	context={
		'form': form,
		'error': error
	}
	return render(request, 'main/log_in.html', context)'''


#def course(request):
	#return render(request, 'main/course.html')


#def stats(request):
	#return render(request, 'main/stats.html')

