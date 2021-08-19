from django.forms import ModelForm, Textarea, TextInput
from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
        widgets = {
            'text': TextInput(attrs={'class': 'input', 'placeholder': 'Say Someting........'})
        }
