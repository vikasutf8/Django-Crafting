from django import forms
from .models import ChaiVarity

class ChaiVarityform(forms.Form):
    chai_varity =forms.MultipleChoiceField(
        queryset=ChaiVarity.objects.all(), label="Select Happy Chai Verity"
    )
    # chai_varity =forms.CharField()