from django import forms
from django.forms import widgets


class PatientCheckInForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    ssn = forms.CharField(max_length=9)


class PatientUpdateProfileForm(forms.Form):
    emergency_contact_name = forms.CharField(max_length=100,required=False)
    emergency_contact_phone = forms.CharField(max_length=15,required=False) # forms.RegexField(regex=r'^\d{10}$')
    address = forms.CharField(max_length=100,required=False)
    zip_code = forms.CharField(max_length=5,required=False)
    cell_phone = forms.CharField(max_length=15,required=False)
