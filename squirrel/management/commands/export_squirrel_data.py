import csv

import datetime

from django.core.management.base import BaseCommand

from squirrel.models import Squirrel

import re

class Command(BaseCommand):
    help = 'Export squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('export_file_name', help = 'the name of the file exported')

    def handle(self, *args, **options):
        file_ = options['export_file_name']

        with open(file_,'w',newline='') as fp:
            writer = csv.writer(fp)
            writer.writerow(['Latitude','Longitude','Unique Squirrel ID','Shift',
                'Date','Age','Primary Color','Location','Specific Location','Running',
                'Chasing','Climbing','Eating','Foraging','Other Activities','Kuks',
                'Quaas','Moans','Tail Flags','Tail Twitches','Approaches','Indifferent',
                'Runs From' ])

            for sq in Squirrel.objects.all().values_list('Latitude','Longitude','Unique_SquirrelID','Shift',
                'Date','Age','Primary_Color','Location','Specific_Location','Running',
                'Chasing','Climbing','Eating','Foraging','Other_Activities','Kuks',
                'Quaas','Moans','Tail_Flags','Tail_Twitches','Approaches','Indifferent',
                'Runs_from'):
                writer.writerow(sq)

            msg = f'You are exporting {file_}'
            self.stdout.write(self.style.SUCCESS(msg))


