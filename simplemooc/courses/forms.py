from django import forms
from django.conf import settings

from simplemooc.core.mail import send_mail_template

from .models import (
    Announcement,
    CategoryCognitiveProcess,
    ChooseCategoryCognitiveProcess,
    ChooseKnowledgeLevel,
    Comment,
    Course,
    CourseTRB,
    CourseRequest,
    KnowledgeLevel,
    Lesson,
    LessonTRB,
    Verb,
    Material,
    MaterialTRB,
)
from .custom_widgets import DateInputType


class AnnouncementForm(forms.ModelForm):

    class Meta:
        model = Announcement
        fields = [
            'title',
            'content',
        ]


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = [
            'name',
            'slug',
            'description',
            'about',
            'image',
        ]


class CourseTRBForm(forms.ModelForm):

    class Meta(CourseForm.Meta):
        model = CourseTRB
        fields = [
            'name',
            'slug',
            'description',
            'about',
            'image',
        ]


class CourseRequestForm(forms.ModelForm):

    class Meta:
        model = CourseRequest
        fields = [
            'name',
            'description',
            'start_date',
            'is_trb',
        ]
        widgets = {
            'start_date': DateInputType(),
        }


class LessonForm(forms.ModelForm):

    class Meta:
        model = Lesson
        fields = [
            'name',
            'description',
            'number',
            'release_date',
        ]
        widgets = {
            'release_date': DateInputType(),
        }


class LessonTRBForm(forms.ModelForm):

    levels = forms.ModelMultipleChoiceField(
        queryset=ChooseKnowledgeLevel.objects.all(),
        label='nível em que o conteúdo será trabalhado',
        help_text='para selecionar mais de 1, segure ctrl e clique no item'
    )

    class Meta:
        model = LessonTRB
        fields = [
            'name',
            'description',
            'number',
            'release_date',
        ]
        widgets = {
            'release_date': DateInputType(),
        }


class KnowledgeLevelForm(forms.ModelForm):

    class Meta:
        model = KnowledgeLevel
        fields = [
            'name',
            'description',
        ]


class AssignKnowledgeLevelForm(forms.Form):
    name = forms.ChoiceField(
        choices=[(c.name, c.name) for c in ChooseKnowledgeLevel.objects.all()],
        label='nome'
    )


class CategoryDCPForm(forms.ModelForm):

    class Meta:
        model = CategoryCognitiveProcess
        fields = [
            'name',
            'description',
        ]


class VerbForm(forms.ModelForm):

    class Meta:
        model = Verb
        fields = [
            'name',
            'educational_goal',
        ]


class VerbFormChoices(forms.ModelForm):

    def __init__(self, choices, *args, **kwargs):
        super(VerbFormChoices, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.ChoiceField(
            choices=choices,
            label='verbo'
        )

    class Meta:
        model = Verb
        fields = [
            'name',
            'educational_goal',
        ]


class ChooseCategoryCognitiveProcessForm(forms.Form):

    name = forms.ChoiceField(
        choices=[
            (c.name, c.name)
            for c in ChooseCategoryCognitiveProcess.objects.all()
        ],
        label='nome'
    )


class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = [
            'name',
            'embedded',
            'material_file',
        ]


class MaterialTRBForm(forms.ModelForm):

    class Meta:
        model = MaterialTRB
        fields = [
            'name',
            'embedded',
            'material_file',
        ]


class ContactCourse(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(
        label='Mensagem/Dúvida',
        widget=forms.Textarea
    )

    def send_mail(self, course):
        subject = '[%s] Contato' % course
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        template_name = 'courses/contact_email.html'
        send_mail_template(
            subject, template_name, context, [settings.CONTACT_EMAIL]
        )


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comment']
