from django.conf import settings
from django.db import models

from simplemooc.core.mail import send_mail_template

from simplemooc.accounts.models import Professor

from .base_models.base import (
    BaseCourse,
    BaseLesson,
    BaseCategoryCognitiveProcess,
    BaseKnowledgeLevel,
    BaseMaterial,
)


class Course(BaseCourse):

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        ordering = ['name']

    @property
    def is_normal_course(self):
        return True


class CourseTRB(BaseCourse):

    class Meta:
        verbose_name = 'curso Taxonomia Revisada de Bloom'
        verbose_name_plural = 'cursos Taxonomia Revisada de Bloom'

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def is_normal_course(self):
        return False


class CourseRequest(models.Model):

    name = models.CharField(
        'nome do curso',
        max_length=150,
    )
    description = models.TextField(
        'descrição curta',
        blank=True
    )
    start_date = models.DateField(
        'Data de início do curso',
        null=True,
        blank=True,
    )
    professor = models.ForeignKey(
        Professor,
        verbose_name='professor',
        related_name='course_requests'
    )
    is_trb = models.BooleanField(
        'Curso usará ferramentas pedagógicas de apoio?',
        default=False
    )
    date_requested = models.DateTimeField(
        'Data da requisição',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "requisição de curso"
        verbose_name_plural = "requisições de cursos"

    def __str__(self):
        return self.name


class Lesson(BaseLesson):
    course = models.ForeignKey(
        Course,
        verbose_name='Curso',
        related_name='lessons'
    )

    class Meta:
        verbose_name = 'aula'
        verbose_name_plural = 'aulas'
        ordering = ['number']


class LessonTRB(BaseLesson):

    course = models.ForeignKey(
        CourseTRB,
        verbose_name='curso utilizando Ferramenta Pedagógica de Apoio',
        related_name='lessonstrb'
    )

    class Meta:
        verbose_name = 'aula curso taxonomia revisada de bloom'
        verbose_name_plural = 'aulas curso taxonomia revisada de bloom'


class ChooseKnowledgeLevel(BaseKnowledgeLevel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'escolha nível de conhecimento'
        verbose_name_plural = 'escolhas níveis de conhecimento'


class KnowledgeLevel(BaseKnowledgeLevel):

    lesson = models.ForeignKey(
        LessonTRB,
        verbose_name='lição',
        related_name='levels'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'nível de conhecimento'
        verbose_name_plural = 'níveis de conhecimento'


class ChooseCategoryCognitiveProcess(BaseCategoryCognitiveProcess):

    class Meta:
        verbose_name = 'escolha da categoria da dimensão processo cognitivo'
        verbose_name_plural = 'escolhas das categorias da dimensão\
        processo cognitivo'


class CategoryCognitiveProcess(BaseCategoryCognitiveProcess):

    lesson = models.ForeignKey(
        LessonTRB,
        verbose_name='lição',
        related_name='categories_dimension'
    )
    level = models.ForeignKey(
        KnowledgeLevel,
        verbose_name='nível de conhecimento',
        related_name='categories_dimension'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoria da dimensão processo cognitivo'
        verbose_name_plural = 'categorias da dimensão processo cognitivo'


class Verb(models.Model):

    CRIAR = (
        ('produzir', 'produzir'),
        ('planejar', 'planejar'),
        ('gerar', 'gerar'),
    )
    AVALIAR = (
        ('criticar', 'criticar'),
        ('verificar', 'verificar'),
    )
    ANALISAR = (
        ('atribuir', 'atribuir'),
        ('organizar', 'organizar'),
        ('diferenciar', 'diferenciar'),
    )
    APLICAR = (
        ('implementar', 'implementar'),
        ('executar', 'executar'),
    )
    ENTENDER = (
        ('explicar', 'explicar'),
        ('comparar', 'comparar'),
        ('inferir', 'inferir'),
        ('resumir', 'resumir'),
        ('classificar', 'classificar'),
        ('exemplificar', 'exemplificar'),
        ('interpretar', 'interpretar'),
    )
    LEMBRAR = (
        ('recordar', 'recordar'),
        ('reconhecer', 'reconhecer'),
    )

    VERBS = {
        'criar': CRIAR,
        'avaliar': AVALIAR,
        'analisar': ANALISAR,
        'aplicar': APLICAR,
        'entender': ENTENDER,
        'lembrar': LEMBRAR,
    }

    name = models.CharField(
        'verbo',
        max_length=100
    )
    educational_goal = models.TextField(
        'objetivo educacional',
        blank=True,
        null=True
    )
    category_dimension = models.ForeignKey(
        CategoryCognitiveProcess,
        verbose_name='categoria da dimensão processo cognitivo',
        related_name='verbs'
    )

    def __str__(self):
        return '{} - {}'.format(self.name, self.category_dimension)

    class Meta:
        verbose_name = 'verbo'
        verbose_name_plural = 'verbos'


class Material(BaseMaterial):

    lesson = models.ForeignKey(
        Lesson,
        verbose_name='aula',
        related_name='materiais'
    )

    class Meta:
        verbose_name = 'material'
        verbose_name_plural = 'materiais'


class MaterialTRB(BaseMaterial):

    lesson = models.ForeignKey(
        LessonTRB,
        verbose_name='aula',
        related_name='materiais'
    )

    class Meta:
        verbose_name = 'material'
        verbose_name_plural = 'materiais'


class Enrollment(models.Model):

    STATUS_CHOICE = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado')
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='usuário',
        related_name='enrollments'
    )
    course = models.ForeignKey(
        Course,
        verbose_name='curso',
        related_name='enrollments'
    )
    status = models.IntegerField(
        'situação',
        choices=STATUS_CHOICE,
        default=1,
        blank=True
    )
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    uptade_at = models.DateTimeField('atualizado em', auto_now=True)

    def active(self):
        self.status = 1
        self.save()

    def is_approved(self):
        return self.status == 1

    def __str__(self):
        return str(self.course)

    class Meta:
        verbose_name = 'inscrição'
        verbose_name_plural = 'inscrições'
        unique_together = (('user', 'course'),)


class Announcement(models.Model):
    course = models.ForeignKey(
        Course,
        verbose_name='curso',
        related_name='announcements'
    )
    title = models.CharField(
        'título',
        max_length=100
    )
    content = models.TextField('conteúdo')
    created_at = models.DateTimeField(
        'criado em',
        auto_now_add=True
    )
    uptade_at = models.DateTimeField(
        'atualizado em',
        auto_now=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'anúncio'
        verbose_name_plural = 'anúncios'
        ordering = ['-created_at']


class Comment(models.Model):
    announcement = models.ForeignKey(
        Announcement,
        verbose_name='anúncio',
        related_name='comments'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='usuário'
    )
    comment = models.TextField('comentário')
    created_at = models.DateTimeField(
        'criado em',
        auto_now_add=True
    )
    uptade_at = models.DateTimeField(
        'atualizado em',
        auto_now=True
    )

    class Meta:
        verbose_name = 'comentário'
        verbose_name_plural = 'comentários'
        ordering = ['created_at']


def post_save_announcement(instance, created, **kwargs):
    subject = instance.title
    context = {
        'announcement': instance,
    }
    template_name = 'courses/announcement_mail.html'
    enrollments = Enrollment.objects.filter(
        course=instance.course, status=1
    )
    for enrollment in enrollments:
        recipient_list = [enrollment.user.email]
        send_mail_template(subject, template_name, context, recipient_list)

models.signals.post_save.connect(
    post_save_announcement, sender=Announcement,
    dispatch_uid='post_save_announcement'
)
