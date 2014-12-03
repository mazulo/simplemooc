from django.shortcuts import render
from simplemooc.courses.models import Course


def index(request):
    template_name = 'courses/index.html'
    courses = Course.objects.all()
    return render(request, template_name, {'courses': courses})


def details(request, pk):
    template_name = 'courses/detail.html'
    course = Course.objects.get(pk=pk)
    return render(request, template_name, {'course': course})
