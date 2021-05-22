from django.shortcuts import redirect, render
from .models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# Students


def students(request):
    if request.method == 'GET':
        students = Students.objects.all()

        contex = {
            'students': students
        }

        return render(request, 'portal/student.html', contex)

    elif request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        student_id = request.POST['student_id']
        cgpa = request.POST['cgpa']

        Students.objects.create(name=name, email=email,
                                student_id=student_id, cgpa=cgpa)

        return HttpResponseRedirect(reverse('students'))


def students_action_handler(request, action, id):
    if action == 'delete':
        student = Students.objects.get(id=id)
        student.delete()
        return HttpResponseRedirect(reverse('students'))

    elif action == 'edit':

        if request.method == 'GET':
            student = Students.objects.get(id=id)

            context = {
                'student': student
            }
            return render(request, 'portal/studentEdit.html', context)

        elif request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            student_id = request.POST['student_id']
            cgpa = request.POST['cgpa']

            student = Students.objects.get(id=id)

            student.name = name
            student.email = email
            student.student_id = student_id
            student.cgpa = cgpa

            student.save()

    return HttpResponseRedirect(reverse('students'))

# Teachers


def teachers(request):

    if request.method == 'GET':
        teachers = Teacher.objects.all()
        context = {
            'teachers': teachers
        }
        return render(request, 'portal/teachers.html', context)

    if request.method == 'POST':
        name = request.POST['name']
        course = request.POST['course']

        Teacher.objects.create(name=name, courses=course)

        return HttpResponseRedirect(reverse('teachers'))


def teachers_action_handler(request, action, id):
    if action == 'delete':
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers'))

    elif action == 'edit':
        if request.method == 'GET':
            teachers = Teacher.objects.get(id=id)
            context = {
                'teachers': teachers
            }

            return render(request, 'portal/teachersEdit.html', context)

        elif request.method == 'POST':
            name = request.POST['name']
            course = request.POST['course']

            teacher = Teacher.objects.get(id=id)

            teacher.name = name
            teacher.courses = course

            teacher.save()
    return HttpResponseRedirect(reverse('teachers'))

# Courses


def courses(request):

    if request.method == 'GET':
        courses = Courses.objects.all()
        context = {
            'courses': courses
        }
        return render(request, 'portal/course.html', context)

    if request.method == 'POST':
        name = request.POST['name']

        Courses.objects.create(name=name)

        return HttpResponseRedirect(reverse('courses'))


def courses_action_handler(request, action, id):
    if action == 'delete':
        courses = Courses.objects.get(id=id)
        courses.delete()
        return HttpResponseRedirect(reverse('courses'))

    elif action == 'edit':
        if request.method == 'GET':
            courses = Courses.objects.get(id=id)
            context = {
                'courses': courses
            }

            return render(request, 'portal/courseEdit.html', context)

        elif request.method == 'POST':
            name = request.POST['name']

            courses = Courses.objects.get(id=id)

            courses.name = name

            courses.save()
    return HttpResponseRedirect(reverse('courses'))
