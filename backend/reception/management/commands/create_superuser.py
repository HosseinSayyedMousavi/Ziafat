
from django.core.management.base import BaseCommand

from decouple import config
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create a superuser if it does not exist'

    def handle(self, *args, **options):
        if not User.objects.filter(username=config('SUPERUSER')).exists():
            User.objects.create_superuser(config('SUPERUSER'),config('SUPEREMAIL'),config('SUPERPASS'))
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
