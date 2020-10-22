from django.core.management.base import BaseCommand

from squirrel.models import Squirrel

import re

class Command(BaseCommand):
    help = 'Delete all squirrel data'

    def handle(self,*agr,**options):
        Squirrel.objects.all().delete()


