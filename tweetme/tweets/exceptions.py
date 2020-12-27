from django import forms
class ContentTooLong(forms.ValidationError):
    def __init__(self, message, code=None, params=None):
        super().__init__(message, code=code, params=params)