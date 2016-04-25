from itertools import chain

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType

from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.contrib.auth.decorators import login_required

from simplemooc.courses.models import (
    Announcement,
    CategoryCognitiveProcess,
    ChooseCategoryCognitiveProcess,
    ChooseKnowledgeLevel,
    Course,
    CourseTRB,
    Enrollment,
    KnowledgeLevel,
    Lesson,
    LessonTRB,
    Material,
    MaterialTRB,
    Verb,
)

from simplemooc.courses.forms import (
    AnnouncementForm,
    AssignKnowledgeLevelForm,
    ChooseCategoryCognitiveProcessForm,
    CommentForm,
    ContactCourse,
    CourseRequestForm,
    LessonTRBForm,
    LessonForm,
    VerbForm,
    VerbFormChoices,
    MaterialForm,
    MaterialTRBForm,
)
from .decorators import enrollment_required
from .utils import format_name, get_course_by_instance


def index(request):
    template_name = 'courses/index.html'
    courses = list(chain(Course.objects.all(), CourseTRB.objects.all()))
    return render(request, template_name, {'courses': courses})


@login_required
def list_courses_trb(request):
    template_name = 'courses/list_courses.html'
    context = {}
    courses = CourseTRB.objects.all()
    context['courses'] = courses
    context['is_trb'] = True
    return render(request, template_name, context)


@login_required
def list_courses_normal(request):
    template_name = 'courses/list_courses.html'
    context = {}
    courses = Course.objects.all()
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
def course_trb(request, pk):
    template_name = 'courses/course.html'
    context = {}
    course = get_object_or_404(CourseTRB, pk=pk)
    context['course'] = course
    return render(request, template_name, context)


@login_required
def create_course_request(request):
    template_name = 'courses/create_course_request.html'
    context = {}

    if request.method == 'POST':
        form = CourseRequestForm(request.POST)
        if form.is_valid():
            course_request = form.save(commit=False)
            course_request.professor = request.user.professor
            course_request.save()
            context['is_valid'] = True
            form = CourseRequestForm()
    else:
        form = CourseRequestForm()

    context['form'] = form

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
    course = get_course_by_instance(slug, Course, CourseTRB)
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
def create_lesson(request, pk):
    template_name = 'courses/create_lesson.html'
    context = {}
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            return redirect('courses:course', pk=pk)
    else:
        form = LessonForm()
    context['form'] = form
    context['course'] = course
    return render(request, template_name, context)


@login_required
def view_lesson(request, pk, lesson_pk):
    context = {}
    template_name = 'courses/view_lesson.html'

    lesson = get_object_or_404(Lesson, pk=lesson_pk)
    course = get_object_or_404(Course, pk=pk)

    context['lesson'] = lesson
    context['course'] = course

    return render(request, template_name, context)


@login_required
def edit_lesson(request, pk, lesson_pk):
    template_name = 'courses/create_lesson.html'
    context = {}
    course = get_object_or_404(Course, pk=pk)
    lesson = get_object_or_404(Lesson, pk=lesson_pk)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('courses:course', pk=pk)
    else:
        form = LessonForm(instance=lesson)
    context['form'] = form
    context['course'] = course
    return render(request, template_name, context)


@login_required
def create_material_lesson(request, c_pk, l_pk):
    template_name = 'courses/create_material.html'
    context = {}

    lesson = get_object_or_404(Lesson, pk=l_pk)

    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.lesson = lesson
            material.save()
            return redirect('courses:view_lesson', pk=c_pk, lesson_pk=l_pk)
    else:
        form = MaterialForm()

    context['form'] = form
    context['lesson'] = lesson
    return render(request, template_name, context)


@login_required
def create_lesson_trb(request, pk):
    template_name = 'courses/create_lesson.html'
    context = {}
    course = get_object_or_404(CourseTRB, pk=pk)
    if request.method == 'POST':
        form = LessonTRBForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course
            lesson.save()
            for level in form.cleaned_data.get('levels'):
                level = KnowledgeLevel.objects.create(
                    name=level.name,
                    description=level.description,
                    lesson=lesson
                )
            # import ipdb; ipdb.set_trace()
            return redirect('courses:course_trb', pk=pk)
    else:
        form = LessonTRBForm()
    context['form'] = form
    context['course'] = course
    context['levels'] = ChooseKnowledgeLevel.objects.all()
    return render(request, template_name, context)


@login_required
def edit_lesson_trb(request, pk, lesson_pk):
    template_name = 'courses/create_lesson.html'
    context = {}
    course = get_object_or_404(CourseTRB, pk=pk)
    lesson = get_object_or_404(LessonTRB, pk=lesson_pk)
    if request.method == 'POST':
        form = LessonTRBForm(request.POST)
        if form.is_valid():
            for level in form.cleaned_data.get('levels'):
                level.lessons.remove(lesson)
                level.lessons.add(lesson)
            # import ipdb; ipdb.set_trace()
            lesson.save()
            return redirect('courses:course_trb', pk=pk)
    else:
        form = LessonTRBForm(instance=lesson)
    context['form'] = form
    context['course'] = course
    return render(request, template_name, context)


@login_required
def view_lesson_trb(request, pk, lesson_pk):
    context = {}
    template_name = 'courses/view_lesson.html'

    lesson = get_object_or_404(LessonTRB, pk=lesson_pk)
    course = get_object_or_404(CourseTRB, pk=pk)

    context['lesson'] = lesson
    context['course'] = course

    return render(request, template_name, context)


@login_required
def create_material_lesson_trb(request, c_pk, l_pk):
    template_name = 'courses/create_material.html'
    context = {}

    lesson = get_object_or_404(LessonTRB, pk=l_pk)

    if request.method == 'POST':
        form = MaterialTRBForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.lesson = lesson
            material.save()
            return redirect('courses:view_lesson_trb', pk=c_pk, lesson_pk=l_pk)
    else:
        form = MaterialTRBForm()

    context['form'] = form
    context['lesson'] = lesson
    return render(request, template_name, context)


@login_required
def add_verb_description(request, course_pk, lesson_pk, cat_pk):
    template_name = 'courses/add_verb_description.html'
    context = {}

    course = get_object_or_404(CourseTRB, pk=course_pk)
    lesson = get_object_or_404(LessonTRB, pk=lesson_pk)
    category = get_object_or_404(CategoryCognitiveProcess, pk=cat_pk)
    name = category.name.lower()

    if request.method == 'POST':
        form = VerbForm(request.POST)
        if form.is_valid():
            verb = form.save(commit=False)
            verb.category_dimension = category
            verb.save()
            return redirect('courses:course_trb', pk=course.pk)
    else:
        form = VerbFormChoices(choices=Verb.VERBS[name])

    context['form'] = form
    context['course'] = course
    context['lesson'] = lesson
    context['category'] = category

    return render(request, template_name, context)


@login_required
def edit_verb_description(request, c_pk, v_pk, cat_pk):
    template_name = 'courses/add_verb_description.html'
    context = {}

    course = get_object_or_404(CourseTRB, pk=c_pk)
    verb = get_object_or_404(Verb, pk=v_pk)
    category = get_object_or_404(CategoryCognitiveProcess, pk=cat_pk)

    if request.method == 'POST':
        form = VerbForm(request.POST, instance=verb)
        if form.is_valid():
            verb = form.save()
            return redirect('courses:course_trb', pk=course.pk)
    else:
        form = VerbForm(instance=verb)

    context['form'] = form
    context['course'] = course
    context['category'] = category

    return render(request, template_name, context)


@login_required
def delete_verb_description(request, c_pk, v_pk):

    course = get_object_or_404(CourseTRB, pk=c_pk)

    Verb.objects.get(pk=v_pk).delete()

    return redirect('courses:course_trb', pk=course.pk)


@login_required
def add_category_cognitive(request, c_pk, l_pk, n_pk):
    template_name = 'courses/add_category_cognitive.html'
    context = {}

    course = get_object_or_404(CourseTRB, pk=c_pk)
    lesson = get_object_or_404(LessonTRB, pk=l_pk)
    level = get_object_or_404(KnowledgeLevel, pk=n_pk)

    if request.method == 'POST':
        form = ChooseCategoryCognitiveProcessForm(request.POST)
        if form.is_valid():
            CategoryCognitiveProcess.objects.create(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                lesson=lesson,
                level=level,
            )
            messages.success(
                request,
                'Sua categoria foi criada com sucesso!'
            )
            return redirect(
                'courses:add_category_cognitive',
                c_pk=course.pk,
                l_pk=lesson.pk,
                n_pk=level.pk,
            )
    else:
        form = ChooseCategoryCognitiveProcessForm()

    context = {
        'form': form,
        'course': course,
        'lesson': lesson,
        'categories': ChooseCategoryCognitiveProcess.objects.all(),
    }

    return render(request, template_name, context)


@login_required
def delete_category_cognitive(request, c_pk, cat_pk):

    course = get_object_or_404(CourseTRB, pk=c_pk)

    CategoryCognitiveProcess.objects.get(pk=cat_pk).delete()

    return redirect('courses:course_trb', pk=course.pk)


@login_required
def add_knowledge_level(request, pk, lesson_pk):
    context = {}
    template_name = 'courses/add_knowledge_level.html'

    lesson = get_object_or_404(LessonTRB, pk=lesson_pk)
    course = get_object_or_404(CourseTRB, pk=pk)

    if request.method == 'POST':
        form = AssignKnowledgeLevelForm(request.POST)
        if form.is_valid():
            # import ipdb; ipdb.set_trace()
            KnowledgeLevel.objects.create(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                lesson=lesson
            )
            return redirect('courses:course_trb', pk=pk)
    else:
        form = AssignKnowledgeLevelForm()
    context['form'] = form
    context['lesson'] = lesson
    context['course'] = course
    context['levels'] = ChooseKnowledgeLevel.objects.all()

    return render(request, template_name, context)


@login_required
def delete_knowledge_level(request, c_pk, n_pk):

    course = get_object_or_404(CourseTRB, pk=c_pk)

    KnowledgeLevel.objects.get(pk=n_pk).delete()

    return redirect('courses:course_trb', pk=course.pk)


@login_required
def get_trb_table(request, c_pk, l_pk):
    template_name = 'courses/get_trb_table.html'
    context = {}

    course = get_object_or_404(CourseTRB, pk=c_pk)
    lesson = get_object_or_404(LessonTRB, pk=l_pk)

    verbs = list()

    for level in lesson.levels.all():
        for category in level.categories_dimension.all():
            verbs_oe = []
            for verb in category.verbs.all():
                oe = verb.educational_goal[:3]
                verbs_oe.append(oe)
                verbs.append(verb)
            context['verbs'] = verbs
            level_name = format_name(level.name)
            category_name = format_name(category.name)
            name_dict = '{}_{}'.format(level_name, category_name)
            context[name_dict] = ', '.join(verbs_oe)

    context['course'] = course
    context['lesson'] = lesson
    return render(request, template_name, context)


@login_required
def enrollment(request, slug):
    course = get_course_by_instance(slug, Course, CourseTRB)
    content_type = ContentType.objects.get_for_model(course)
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=course.id,
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
def create_announcement(request, course_slug):
    context = {}
    template_name = 'courses/create_announcement.html'
    course = get_course_by_instance(course_slug, Course, CourseTRB)
    content_type = ContentType.objects.get_for_model(course)

    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            Announcement.objects.create(
                content_type=content_type,
                object_id=course.id,
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
            )
            return redirect('courses:create_announcement', course.slug)
    else:
        form = AnnouncementForm()

    context['course'] = course
    context['form'] = form
    return render(request, template_name, context)


@login_required
def list_announcements(request, course_slug):
    template = 'courses/announcements.html'
    course = get_course_by_instance(course_slug, Course, CourseTRB)
    context = {
        'course': course,
        'announcements': course.announcements.all()
    }
    return render(request, template, context)


@login_required
def show_announcement_to_professor(request, course_slug, announcement_pk):
    course = get_course_by_instance(course_slug, Course, CourseTRB)
    announcement = get_object_or_404(
        course.announcements.all(), pk=announcement_pk
    )
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.announcement = announcement
        comment.save()
        messages.success(request, 'Seu comentário foi enviado com sucesso')
        form = CommentForm()
    template_name = 'courses/show_announcement.html'
    context = {
        'course': course,
        'announcement': announcement,
        'form': form
    }
    return render(request, template_name, context)


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
    if isinstance(course, CourseTRB):
        lesson = get_object_or_404(LessonTRB, pk=pk, course=course)
    else:
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
def show_material_to_professor(request, course_slug, pk):
    course = get_course_by_instance(course_slug, Course, CourseTRB)
    try:
        if isinstance(course, CourseTRB):
            material = MaterialTRB.objects.get(pk=pk, lesson__course=course)
        else:
            material = Material.objects.get(
                pk=pk, lesson__course=course
            )
    except (Material.DoesNotExist, MaterialTRB.DoesNotExist):
        messages.error(request, 'Este material não está disponível')
        redirect('courses:lessons', slug=course.slug)
    lesson = material.lesson
    if not material.is_embedded():
        return redirect(material.material_file.url)
    template = 'courses/material.html'
    context = {
        'course': course,
        'lesson': lesson,
        'material': material
    }
    return render(request, template, context)


@login_required
@enrollment_required
def material(request, slug, pk):
    course = request.course
    try:
        if isinstance(course, CourseTRB):
            material = MaterialTRB.objects.get(pk=pk, lesson__course=course)
        else:
            material = material = Material.objects.get(
                pk=pk, lesson__course=course
            )
    except (Material.DoesNotExist, MaterialTRB.DoesNotExist):
        messages.error(request, 'Este material não está disponível')
        redirect('courses:lessons', slug=course.slug)
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
