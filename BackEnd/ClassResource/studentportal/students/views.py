import students
from django.shortcuts import redirect, render
from django.http import HttpResponse
from students.models import *


def all_students(request):
    if request.method == "GET":
        students = Student.objects.all()
        context = {
            'all_students': students
        }
        return render(request, 'students/index.html', context)

    elif request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone_number = "0174552563"

        Student.objects.create(name=name, email=email, phone=phone_number)

        return redirect('/')


def action_handler(request, action, sid):
    if action == 'delete':
        # Get the student to be deleted
        student = Student.objects.get(id=sid)

        # Delete the student
        student.delete()

    elif action == 'edit':
        if request.method == 'GET':
            student = Student.objects.get(id=sid)
            context = {
                'student': student
            }
            return render(request, 'students/edit.html', context)
        if request.method == 'POST':
            # Get the form data
            input_name = request.POST["name"]
            input_email = request.POST["email"]

            # Get the student to be edited
            student = Student.objects.get(id=sid)

            # Update the values
            student.name = input_name
            student.email = input_email

            # Save the student to the database
            student.save()

    return redirect('/')
