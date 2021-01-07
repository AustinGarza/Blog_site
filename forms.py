from django import forms
from .models import Blog_post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Blog_post
        fields = ['title', 'body']
        labels = {'title': 'title','body': 'body' }
        widgets = {'body': forms.Textarea(attrs={'rows':30, 'cols':100})}
        