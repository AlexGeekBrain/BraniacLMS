from django.core.management import BaseCommand
from mainapp.models import News


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        new_objects = []
        for i in range(10):
            new_objects.append(
                News(
                    title=f'news#{i}',
                    preamble=f'preamble#{i}',
                    body=f'body#{i}'
                )
            )
        News.objects.bulk_create(new_objects)
