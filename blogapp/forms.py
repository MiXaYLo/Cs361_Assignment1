from django import forms
from .models import my_entries

class BlogForm(forms.ModelForm):

    class Meta:
        model = my_entries
        fields = ["header", "body", "tags"]