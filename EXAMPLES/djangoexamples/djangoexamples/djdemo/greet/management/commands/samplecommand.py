from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Sample Command"


    def handle(self, *args, **options):
        self.stdout.write("sample admin command from the 'greet' app\n")

