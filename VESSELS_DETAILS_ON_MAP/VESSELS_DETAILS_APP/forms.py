from django import forms
from .models import RouteDetails

class VesselNumberForm(forms.Form):
    vessel_number = forms.ModelChoiceField(queryset=RouteDetails.objects.all().values_list('vessel_number', flat=True))
