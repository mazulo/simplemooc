from django.shortcuts import render
from simplemooc.courses.models import Course


def index(request):
    template_name = 'courses/index.html'
    courses = Course.objects.all()
    return render(request, template_name, {'courses': courses})
