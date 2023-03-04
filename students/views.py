from django.shortcuts import render
from .models import Student
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all() #students bhanne ma Student class ko all of the table cha
    })

def student_view(request , id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))