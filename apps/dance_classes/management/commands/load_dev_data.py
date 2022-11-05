from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils import timezone

from dance_classes.models import DanceClass


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Delete all database records
        call_command("flush", interactive=False)

        # Create `DanceClass` records for 10 weeks
        for i in range(10):
            DanceClass.objects.create(
                teacher="Alex",
                location="Long Beach",
                date=timezone.now() + timezone.timedelta(days=i * 7),
            )
