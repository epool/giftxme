from django import forms
from models import Exchange

class ParticipantsForm(forms.Form):
    organizerName = forms.CharField()
    organizerEmail = forms.EmailField()
    participant1Name = forms.CharField()
    participant1Email = forms.EmailField()
    participant2Name = forms.CharField()
    participant2Email = forms.EmailField()

class ExchangeForm(forms.ModelForm):
    class Meta:
        model = Exchange