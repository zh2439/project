import csv

import datetime

from django.core.management.base import BaseCommand

from squirrel.models import Squirrel

import re

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
                obj.Unique_SquirrelID = item['Unique Squirrel ID']
                obj.Shift = item['Shift']
                obj.Date = datetime.date(int(item['Date'][-4:]),int(item['Date'][:2]),int(item['Date'][2:4]))
                obj.Age = item['Age']
                obj.Primary_Color = item['Primary Fur Color']
                obj.location = item['Location']
                obj.Specific_Location = item['Specific Location']
                obj.Running = True if item['Running'] == 'true' else False
                obj.Chasing = True if item['Chasing'] == 'true' else False
                obj.Climbing = True if item['Climbing'] == 'true' else False
                obj.Eating = True if item['Eating'] == 'true' else False
                obj.Foraging = True if item['Foraging'] == 'true' else False
                obj.Other_activities = item['Other Activities']
                obj.Kuks = True if item['Kuks'] == 'true' else False
                obj.Quaas = True if item['Quaas'] == 'true' else False
                obj.Moans = True if item['Moans'] == 'true' else False
                obj.Tail_Flags = True if item['Tail flags'] == 'true' else False
                obj.Tail_Twitches = True if item['Tail twitches'] == 'true' else False
                obj.Approaches = True if item['Approaches'] == 'true' else False
                obj.Indifferent = True if item['Indifferent'] == 'true' else False
                obj.Runs_From = True if item['Runs from'] == 'true' else False

                try:
                    obj.save()
                except Exception as e:
                    msg1=f'ERROR:{e}at{obj.Unique_SquirrelID}'
                    self.stdout.write(self.style.ERROR(msg1))

            msg = f'You are importing from {file_}'

            self.stdout.write(self.style.SUCCESS(msg))
