from django.shortcuts import render, get_object_or_404
from simplemooc.courses.models import Course


def index(request):
    template_name = 'courses/index.html'
    courses = Course.objects.all()
    return render(request, template_name, {'courses': courses})


# Method via pk
# def details(request, pk):
#     template_name = 'courses/detail.html'
#     course = get_object_or_404(Course, pk=pk)
#     return render(request, template_name, {'course': course})


def details(request, slug):
    template_name = 'courses/detail.html'
    course = get_object_or_404(Course, slug=slug)
    return render(request, template_name, {'course': course})
