from django.contrib import admin

# Register your models here.
from .models import (
    Course,
    CourseTRB,
    Announcement,
    Comment,
    Enrollment,
    Lesson,
    LessonTRB,
    Material,
    KnowledgeLevel,
    CategoryDimensionCognitiveProcess,
    Verb,
)


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ['name']}


class CourseTRBAdmin(CourseAdmin):
    pass


class MaterialInlineAdmin(admin.StackedInline):

    model = Material


class LessonAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'course', 'release_date']
    search_fields = ['name', 'description']
    list_filter = ['created_at']

    inlines = [
        MaterialInlineAdmin
    ]


admin.site.register(Course, CourseAdmin)
admin.site.register(CourseTRB, CourseTRBAdmin)
admin.site.register([Enrollment, Announcement, Comment, Material])
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LessonTRB, LessonAdmin)
admin.site.register(KnowledgeLevel)
admin.site.register(CategoryDimensionCognitiveProcess)
admin.site.register(Verb)
