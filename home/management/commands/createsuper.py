from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Create Super-User')
        User.objects.create_superuser('admin','admin@admin.com','gring21!')