from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post, Tag
from .models import Comment

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags separated by commas.")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        tags_str = self.cleaned_data.get('tags', '')
        tag_names = [t.strip() for t in tags_str.split(',') if t.strip()]
        tag_objects = []
        for tag_name in tag_names:
            tag_obj, created = Tag.objects.get_or_create(name=tag_name)
            tag_objects.append(tag_obj)
        instance.tags.set(tag_objects)
        return instance


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomUserCreationForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'}),
        }
