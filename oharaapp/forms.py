from django.forms import ModelForm
from .models import Tokuten_post

class TokutenForm(ModelForm):
    class Meta:
        model = Tokuten_post
        fields = ['subject', 'num']