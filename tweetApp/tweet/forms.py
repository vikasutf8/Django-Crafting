from django import forms
from .models import Tweet

#using inbuild forms
class TweetForm(forms.ModelForm):
    class Meta:
        model =Tweet
        fields =['text','photos']