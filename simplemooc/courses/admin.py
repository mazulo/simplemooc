from django.contrib import admin

# Register your models here.
from .models import (
    Course,
    CourseTRB,
    CourseRequest,
    Announcement,
    Comment,
    Enrollment,
    Lesson,
    LessonTRB,
    Material,
    KnowledgeLevel,
    ChooseKnowledgeLevel,
    ChooseCategoryCognitiveProcess,
    CategoryCognitiveProcess,
    Verb,
)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}


class CourseTRBAdmin(CourseAdmin):
    pass


class CourseRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'start_date', 'professor', 'is_trb']
    search_fields = ['name', 'professor']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'course', 'release_date']
    search_fields = ['name', 'description']
    list_filter = ['created_at']


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseTRB, CourseTRBAdmin)
admin.site.register(CourseRequest, CourseRequestAdmin)
admin.site.register([Enrollment, Announcement, Comment, Material])
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonTRB, LessonAdmin)
admin.site.register(KnowledgeLevel)
admin.site.register(ChooseKnowledgeLevel)
admin.site.register(CategoryCognitiveProcess)
admin.site.register(ChooseCategoryCognitiveProcess)
admin.site.register(Verb)
