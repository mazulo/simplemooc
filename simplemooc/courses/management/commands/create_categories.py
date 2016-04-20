from django.core.management.base import BaseCommand, CommandError
from simplemooc.courses.models import ChooseCategoryCognitiveProcess

from ._categories import CATEGORIES


class Command(BaseCommand):

    help = 'Create default knowledge levels for the app'

    def handle(self, *args, **kwargs):
        list_categories = []

        if ChooseCategoryCognitiveProcess.objects.all():
            raise CommandError('Categorias já criadas')
        else:
            for category in CATEGORIES:
                list_categories.append(
                    ChooseCategoryCognitiveProcess(
                        name=category['name'],
                        description=category['description']
                    )
                )
            ChooseCategoryCognitiveProcess.objects.bulk_create(list_categories)
            self.stdout.write('Categorias criados com sucesso.')
