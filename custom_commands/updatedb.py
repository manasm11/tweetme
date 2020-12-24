from os import system
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Runs './manage.py makemigrations' and './manage.py migrate' in conjunction"

    def handle(self, *test_labels, **options):
        system("./manage.py makemigrations")
        system("./manage.py migrate")
