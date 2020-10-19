import csv

import datetime

from django.core.management.base import BaseCommand

from squirrel.models import Squirrel

class Command(BaseCommand):
    help = 'Get squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_file', help = 'file containing squirrel data')

    def handle(self, *args, **options):
        file_ = options['squirrel_file']

        with open(file_) as fp:
            reader = csv.DictReader(fp)

            for item in reader:
                obj = Squirrel()
                obj.Latitude = item['X']
                obj.Longitude = item['Y']
                obj.Unique_Squirrel_ID = item['Unique Squirrel ID']
                obj.Shift = item['Shift']
                obj.Date = datetime.date(int(item['Date'][-4:]),int(item['Date'][:2]),int(item['Date'][2:4]))
                obj.Age = item['Age']

                obj.save()

            msg = f'You are importing from {file_}'

            self.stdout.write(self.style.SUCCESS(msg))
