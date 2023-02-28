from django.shortcuts import render
from .models import Student

def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all() #students bhanne ma Student class ko all of the table cha
    })