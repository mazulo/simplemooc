from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType

from .models import Course, CourseTRB, Enrollment
from .utils import get_course_by_instance


def enrollment_required(view_func):
    def _wrapper(request, *args, **kwargs):
        slug = kwargs['slug']
        course = get_course_by_instance(slug, Course, CourseTRB)
        content_type = ContentType.objects.get_for_model(course)
        has_permission = request.user.is_staff
        if not has_permission:
            try:
                enrollment = Enrollment.objects.get(
                    content_type=content_type,
                    object_id=course.id,
                    user=request.user
                )
            except Enrollment.DoesNotExist:
                message = 'Desculpe, mas você não tem permissão de acesso'
            else:
                if enrollment.is_approved():
                    has_permission = True
                else:
                    message = 'Sua inscrição do curso ainda está pendente'
        if not has_permission:
            messages.error(request, message)
            return redirect('accounts:dashboard')
        request.course = course
        return view_func(request, *args, **kwargs)
    return _wrapper
