from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from simplemooc.courses.models import (
    Course,
    Enrollment,
    Lesson,
    Material
)
from simplemooc.courses.forms import (
    ContactCourse,
    CommentForm,
    LessonForm,
    LessonTRBForm,
    KnowledgeLevelForm,
    CourseForm,
    CourseTRBForm
)
from .decorators import enrollment_required


def index(request):
    template_name = 'courses/index.html'
    courses = Course.objects.all()
    return render(request, template_name, {'courses': courses})


@login_required
def list_courses_trb(request):
    template_name = 'courses/list_courses.html'
    context = {}
    courses = Course.course_objects.courses_trb()
    context['courses'] = courses
    context['is_trb'] = True
    return render(request, template_name, context)


@login_required
def list_courses_normal(request):
    template_name = 'courses/list_courses.html'
    context = {}
    courses = Course.course_objects.courses_normal()
    context['courses'] = courses
    context['is_trb'] = False
    return render(request, template_name, context)


@login_required
def course(request, pk):
    template_name = 'courses/course.html'
    context = {}
    course = get_object_or_404(Course, pk=pk)
    context['course'] = course
    return render(request, template_name, context)


@login_required
def edit_course(request, pk):
    template_name = ''
    context = {}
    # course = get_object_or_404(Course, pk=pk)
    return render(request, template_name, context)


def details(request, slug):
    template_name = 'courses/detail.html'
    context = {}
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['course'] = course
    context['form'] = form
    return render(request, template_name, context)


@login_required
def enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user,
        course=course
    )
    if created:
        messages.success(request, 'Sua inscrição foi realizada com sucesso')
    else:
        messages.info(request, 'Você já está inscrito nesse curso')
    return redirect('accounts:dashboard')


@login_required
def undo_enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment = get_object_or_404(
            Enrollment,
            user=request.user,
            course=course
    )
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, 'Sua inscrição foi cancelada com sucesso.')
        return redirect('accounts:dashboard')
    template = 'courses/undo_enrollment.html'
    context = {
        'enrollment': enrollment,
        'course': course
    }
    return render(request, template, context)


@login_required
@enrollment_required
def announcements(request, slug):
    course = request.course
    template = 'courses/announcements.html'
    context = {
        'course': course,
        'announcements': course.announcements.all()
    }
    return render(request, template, context)


@login_required
@enrollment_required
def show_announcement(request, slug, pk):
    course = request.course
    announcement = get_object_or_404(course.announcements.all(), pk=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.announcement = announcement
        comment.save()
        messages.success(request, 'Seu comentário foi enviado com sucesso')
        form = CommentForm()
    template = 'courses/show_announcement.html'
    context = {
        'course': course,
        'announcement': announcement,
        'form': form
    }
    return render(request, template, context)


@login_required
@enrollment_required
def lessons(request, slug):
    course = request.course
    template = 'courses/lessons.html'
    lessons = course.release_lessons()
    if request.user.is_staff:
        lessons = course.lessons.all()
    context = {
        'course': course,
        'lessons': lessons
    }
    return render(request, template, context)


@login_required
@enrollment_required
def lesson(request, slug, pk):
    course = request.course
    lesson = get_object_or_404(Lesson, pk=pk, course=course)
    if not request.user.is_staff and not lesson.is_available():
        messages.error(request, 'Esta aula não está disponível')
        redirect('courses:lessons', slug=course.slug)
    template = 'courses/lesson.html'
    context = {
        'course': course,
        'lesson': lesson
    }
    return render(request, template, context)


@login_required
@enrollment_required
def material(request, slug, pk):
    course = request.course
    material = get_object_or_404(Material, pk=pk, lesson__course=course)
    lesson = material.lesson
    if not request.user.is_staff and not lesson.is_available():
        messages.error(request, 'Este material não está disponível')
        redirect('courses:lesson', slug=course.slug, pk=lesson.pk)
    if not material.is_embedded():
        return redirect(material.material_file.url)
    template = 'courses/material.html'
    context = {
        'course': course,
        'lesson': lesson,
        'material': material
    }
    return render(request, template, context)
