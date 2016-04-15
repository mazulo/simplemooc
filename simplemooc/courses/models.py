from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from .managers import KindOfCourse
from simplemooc.core.mail import send_mail_template
from simplemooc.accounts.models import Professor


class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )


class Course(models.Model):
    name = models.CharField(
        'nome',
        max_length=100
    )
    slug = models.SlugField('atalho')
    description = models.TextField(
        'descrição curta',
        blank=True
    )
    about = models.TextField(
        'sobre o curso',
        blank=True
    )
    created_at = models.DateTimeField(
        'criado em',
        auto_now_add=True
    )
    uptade_at = models.DateTimeField(
        'atualizado em',
        auto_now=True
    )
    start_date = models.DateField(
        'data de início',
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='courses/images',
        verbose_name='imagem',
        null=True,
        blank=True
    )
    professor = models.ForeignKey(
        Professor,
        verbose_name='professor',
        related_name='courses'
    )
    objects = CourseManager()
    course_objects = KindOfCourse.as_manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses:details', args=[str(self.slug)])

    def release_lessons(self):
        today = timezone.now().date()
        return self.lessons.filter(release_date__gte=today)

    @property
    def is_trb(self):
        return hasattr(self, 'course_trb')

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        ordering = ['name']


class CourseTRB(Course):

    def __str__(self):
        return '{}-TRB'.format(self.name)

    class Meta:
        verbose_name = 'curso Taxonomia Revisada de Bloom'
        verbose_name_plural = 'cursos Taxonomia Revisada de Bloom'


class KnowledgeLevel(models.Model):
    name = models.CharField(
        'nome',
        max_length=100
    )
    description = models.TextField(
        'descrição',
        blank=True
    )

    class Meta:
        verbose_name = 'nível de conhecimento'
        verbose_name_plural = 'níveis de conhecimento'


class CategoryDimensionCognitiveProcess(models.Model):
    name = models.CharField(
        'nome',
        max_length=100
    )
    description = models.TextField(
        'descrição',
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'categoria da dimensão processo cognitivo'
        verbose_name_plural = 'categorias da dimensão processo cognitivo'


class Verb(models.Model):
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
        CategoryDimensionCognitiveProcess,
        verbose_name='categoria da dimensão processo cognitivo',
        related_name='verbs'
    )

    def __str__(self):
        return '{} - {}'.format(self.name, self.category_dimension)

    class Meta:
        verbose_name = 'verbo'
        verbose_name_plural = 'verbos'


class Lesson(models.Model):
    name = models.CharField(
        'nome',
        max_length=100
    )
    description = models.TextField(
        'descrição',
        blank=True
    )
    number = models.IntegerField(
        'número (ordem)',
        blank=True,
        default=0
    )
    release_date = models.DateField(
        'data de liberação',
        blank=True,
        null=True
    )
    course = models.ForeignKey(
        Course,
        verbose_name='Curso',
        related_name='lessons'
    )
    created_at = models.DateTimeField(
        'criado em',
        auto_now_add=True
    )
    uptade_at = models.DateTimeField(
        'atualizado em',
        auto_now=True
    )

    def __str__(self):
        return self.name

    def is_available(self):
        if self.release_date:
            today = timezone.now().date()
            return self.release_date >= today
        return False

    class Meta:
        verbose_name = 'aula'
        verbose_name_plural = 'aulas'
        ordering = ['number']


class LessonTRB(Lesson):

    category_dimension = models.ManyToManyField(
        CategoryDimensionCognitiveProcess,
        verbose_name='categoria processo cognitivo',
        related_name='lessons'
    )
    levels = models.ManyToManyField(
        KnowledgeLevel,
        verbose_name='levels',
        related_name='lessons'
    )

    class Meta:
        verbose_name = 'aula curso taxonomia revisada de bloom'
        verbose_name_plural = 'aulas curso taxonomia revisada de bloom'


class Material(models.Model):
    name = models.CharField(
        'nome',
        max_length=100
    )
    embedded = models.TextField(
        'vídeo embedded',
        blank=True
    )
    material_file = models.FileField(
        upload_to='lessons/material',
        blank=True,
        null=True
    )

    lesson = models.ForeignKey(
        Lesson,
        verbose_name='aula',
        related_name='materiais'
    )

    def is_embedded(self):
        return bool(self.embedded)

    def __str__(self):
        return self.name

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
