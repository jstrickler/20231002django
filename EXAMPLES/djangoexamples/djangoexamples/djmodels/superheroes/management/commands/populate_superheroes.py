import yaml
from django.core.management.base import BaseCommand
from superheroes.models import Superhero, Enemy, Power, City


class Command(BaseCommand):
    help = "Populates the superhero database"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Successfully populated superheroes'))
