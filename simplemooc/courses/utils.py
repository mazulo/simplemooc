def format_name(name):
    if name.count('/'):
        return name.replace('/', '_').lower()
    elif name.count(' '):
        return name.replace(' ', '_').lower()
    return name.lower()


def get_course_by_instance(course_slug, Course, CourseTRB):
    try:
        course = Course.objects.get(slug=course_slug)
    except Course.DoesNotExist:
        course = CourseTRB.objects.get(slug=course_slug)
    return course
