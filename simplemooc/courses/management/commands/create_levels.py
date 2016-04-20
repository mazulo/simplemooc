from django.core.management.base import BaseCommand, CommandError
from simplemooc.courses.models import ChooseKnowledgeLevel

from ._levels import LEVELS


class Command(BaseCommand):

    help = 'Create default knowledge levels for the app'

    def handle(self, *args, **kwargs):
        list_levels = []

        if ChooseKnowledgeLevel.objects.all():
            raise CommandError('Níveis já criados')
        else:
            for level in LEVELS:
                list_levels.append(
                    ChooseKnowledgeLevel(
                        name=level['name'],
                        description=level['description']
                    )
                )
            ChooseKnowledgeLevel.objects.bulk_create(list_levels)
            self.stdout.write('Níveis criados com sucesso.')
