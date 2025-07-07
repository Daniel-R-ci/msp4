from django import forms
from .models import Article_Comment


class Article_Comment_Form(forms.ModelForm):
    class Meta:
        model = Article_Comment
        fields = ('comment', 'image')
