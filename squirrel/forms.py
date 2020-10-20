from django.forms import ModelForm

from .models import Squirrel

class Update(ModelForm):
    class Meta:
        model=Squirrel
        fields = [
                'Latitude',
                'Longitude',
                'Unique_SquirrelID',
                'Shift',
                'Date',
                'Age',
        ]
        extra_kwargs = {'__all__': {'required': False}}

