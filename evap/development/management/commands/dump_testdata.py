import os

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    args = ""
    help = "Dumps all relevant contents of the database into test_data.json."
    requires_migrations_checks = True

    def handle(self, *args, **options):
        outfile_name = os.path.join(settings.BASE_DIR, "development", "fixtures", "test_data.json")
        call_command(
            "dumpdata",
            "auth.group",
            "evaluation",
            "rewards",
            "student",
            "grades",
            "--exclude=evaluation.LogEntry",
            indent=2,
            output=outfile_name,
            natural_foreign=True,
            natural_primary=True,
        )
