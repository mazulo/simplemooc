from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from simplemooc.accounts.models import Professor


class CourseManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) |
            models.Q(description__icontains=query)
        )


class BaseCourse(models.Model):
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
        related_name='%(app_label)s_%(class)s_courses'
    )
    objects = CourseManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('courses:details', args=[str(self.slug)])

    def release_lessons(self):
        today = timezone.now().date()
        return self.lessons.filter(release_date__gte=today)

    class Meta:
        abstract = True
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        ordering = ['name']


class BaseLesson(models.Model):
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
        abstract = True
        verbose_name = 'aula'
        verbose_name_plural = 'aulas'
        ordering = ['number']


class BaseCategoryCognitiveProcess(models.Model):
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
        abstract = True
        verbose_name = 'categoria da dimensão processo cognitivo'
        verbose_name_plural = 'categorias da dimensão processo cognitivo'


class BaseKnowledgeLevel(models.Model):
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
        abstract = True
        verbose_name = 'nível de conhecimento'
        verbose_name_plural = 'níveis de conhecimento'


class BaseMaterial(models.Model):
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

    def is_embedded(self):
        return bool(self.embedded)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        verbose_name = 'material'
        verbose_name_plural = 'materiais'
