from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    Latitude = models.CharField(
            max_length=100,
            help_text=_('latitude of squirrel'),
    )

    Longitude = models.CharField(
            max_length=100,
            help_text=_('longitude of squirrel'),
    )

    Unique_ID = models.CharField(
            max_length=100,
            help_text=_('unique squirrel id of squirrel'),
    )


    Shift = models.CharField(
            max_length=100,
            help_text=_('shift of squirrel'),
    )

    Date = models.DateField(
            help_text=_('date of squirrel'),
    )


    Age = models.CharField(
            max_length=100,
            help_text=_('age of squirrel'),
    )
