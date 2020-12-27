from django import forms
from .models import TweetModel
from . import exceptions
from django.conf import settings
MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH
class TweetForm(forms.ModelForm):
    class Meta:
        model = TweetModel
        fields = ['content']
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            print("******ERROR SHOULD HAVE BEEN SAISED")
            raise forms.ValidationError("Tweet is too long")
        return content