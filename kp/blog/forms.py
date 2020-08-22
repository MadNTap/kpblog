from .models import Post
from django import forms
from django_summernote.fields import SummernoteTextField


class NewBlogPost(forms.ModelForm):
    foo = SummernoteTextField()
