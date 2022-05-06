from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Course, Subcourse


def index(request):
    return render(request, 'index.html')


def course(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'title':'Курсы', 'courses':courses})


def stats(request):
    return render(request, 'stats.html')


def subcourse(request, course_id):
    c = get_object_or_404(Course, pk=course_id)
    subcourses = c.subcourse_set.all()

    return render(request, 'subcourse.html', {'title': 'Подкурсы', 'subcourses':subcourses})


