from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    Latitude = models.FloatField(
            max_length=100,
            help_text=_('*To eight decimal places'),
    )

    Longitude = models.FloatField(
            max_length=100,
            help_text=_('*To eight decimal places'),
    )

    Unique_SquirrelID = models.CharField(
            max_length=100,
            unique=True,
            help_text=_('*Hectare-Shift-mmdd-Hectare Squirrel Number. e.g. "37F-PM-1014-03"'),
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
            help_text=_('*Please select'),
    )

    Date = models.DateField(
            help_text=_('*yyyy-mm-dd'),
    )

    ADULT='Adult'
    JUVENILE='Juvenile'
    UNKNOWN='Unknown'
    
    AGE_CHOICES=[
            (ADULT,_('Adult')),
            (JUVENILE,_('Juvenile')),
            (UNKNOWN,_('Unknown')),
    ]

    Age = models.CharField(
            max_length=100,
            help_text=_('Please select'),
            choices=AGE_CHOICES,
            default=UNKNOWN,
            null=True,
            blank=True,
    )

    BLACK='Black'
    GREY='Grey'
    CINNAMON='Cinnamon'

    PRI_COLOR_CHOICES=[
            (BLACK,_('Black')),
            (GREY,_('Grey')),
            (CINNAMON,_('Cinnamon')),
    ]

    Primary_Color=models.CharField(
            max_length=100,
            help_text=_('Please select'),
            choices=PRI_COLOR_CHOICES,
            null=True,
            blank=True,
    )

    GROUND_PLANE='Ground Plane'
    ABOVE_GROUND='Above Ground'

    LOCA_CHOICES=[ 
            (GROUND_PLANE,_('Ground Plane')),
            (ABOVE_GROUND,_('Above Ground')),
    ]

    Location=models.CharField(
            max_length=100,
            help_text=_('Please select'),
            choices=LOCA_CHOICES,
            null=True,
            blank=True,
    )

    Specific_Location=models.TextField(
            blank=True,
            help_text=_('Describe the specific location'),
    )

    Running=models.BooleanField(
            default=False,
            help_text=_('Whether or not the squirrel is running'),
    )

    Chasing=models.BooleanField(
            default=False,
            help_text=_('Whether or not the squirrel is chasing'),
    )

    Climbing=models.BooleanField(
            default=False,
            help_text=_('Whether or not the squirrel is climbing'),
    )

    Eating=models.BooleanField(
            default=False,
            help_text=_('Whether or not the squirrel is eating'),
    )

    Foraging=models.BooleanField(
            default=False,
            help_text=_('Whether or not the squirrel is foraging'),
    )

    Other_Activities= models.TextField(
            blank=True,
            help_text=_('Describe the specific activity'),
    )

    Kuks=models.BooleanField(
            default=False,
            help_text=_('Whether or not the squirrel kuks'),
    )

    Quaas=models.BooleanField(
            default=False,
            help_text=_('Whether or not the squirrel quaas'),
    )

    Moans=models.BooleanField(
            default=False,
            help_text=_('Whether or not the squirrel moans'),
    )

    Tail_Flags=models.BooleanField(
            default=False,
            help_text=_('Whether or not the tail flags'),
    )

    Tail_Twitches=models.BooleanField(
            default=False,
            help_text=_('Whether or not the tail twitches'),
    )

    Approaches=models.BooleanField(
            default=False,
            help_text=_('Whether or not the squirrel approaches you'),
    )

    Indifferent=models.BooleanField(
            default=False,
            help_text=_('Whether or not the squirrel is indifferent to you'),
    )

    Runs_from=models.BooleanField(
            default=False,
            help_text=_('Whether or not the squirrel runs from you'),
    )

    def __str__(self):
        return self.Unique_SquirrelID

class Meta:
    managed = True
