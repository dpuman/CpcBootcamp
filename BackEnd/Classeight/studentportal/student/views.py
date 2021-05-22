from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from student.models import *


# Create your views here.


def home(request):
    if request.method == 'GET':
        students = student.objects.all()
        contex = {
            'students': students
        }

        return render(request, 'student/home.html', contex)

    elif request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        student_id = request.POST['student_id']
        cgpa = request.POST['cgpa']

        student.objects.create(name=name, email=email,
                               student_id=student_id, cgpa=cgpa)

        return HttpResponseRedirect(reverse("home"))


def teachers(request):

    if request.method == 'GET':
        teachers = Teacher.objects.all()
        context = {
            'teachers': teachers


        }

        return render(request, 'student/teacher.html', context)

    elif request.method == 'POST':
        name = request.POST['name']
        course = request.POST['course']

        Teacher.objects.create(name=name, courses=course)

        return HttpResponseRedirect(reverse('teacher'))


def courses(request):
    if request.method == 'GET':
        courses = Courses.objects.all()

        contex = {
            "courses": courses
        }

        return render(request, 'student/courses.html', contex)
    elif request.method == 'POST':
        name = request.POST['name']

        Courses.objects.create(name=name)

        return HttpResponseRedirect(reverse('courses'))
