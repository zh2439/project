from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    Latitude = models.FloatField(
            max_length=100,
            help_text=_('latitude of squirrel'),
    )

    Longitude = models.FloatField(
            max_length=100,
            help_text=_('longitude of squirrel'),
    )

    Unique_SquirrelID = models.CharField(
            max_length=100,
            unique=True,
            help_text=_('unique squirrel id of squirrel'),
            null=True,
            blank=True,
    )


    AM='AM'
    PM='PM'
    SHIFT_CHOICES =[
            (PM,_('PM')),
            (AM,_('AM')),
    ]

    Shift = models.CharField(
            max_length=100,
            choices=SHIFT_CHOICES,
            help_text=_('shift of squirrel'),
    )

    Date = models.DateField(
            help_text=_('mmddyyyy'),
    )

    ADULT='Adult'
    JUVENILE='Juvenile'
    UNKNOWN='?'
    
    AGE_CHOICES=[
            (ADULT,_('Adult')),
            (JUVENILE,_('Juvenile')),
            (UNKNOWN,_('Unknown')),
    ]

    Age = models.CharField(
            max_length=100,
            help_text=_('age of squirrel'),
            choices=AGE_CHOICES,
            blank = True,
    )

    def __str__(self):
        return self.Unique_SquirrelID

class Meta:
    managed = True
