from django import forms
from .models import DataGather


class AddPostForm(forms.ModelForm):
    class Meta:
        model = DataGather
        exclude = ("author", "slug")
