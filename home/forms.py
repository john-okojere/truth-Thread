from django import forms
from . import models

class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ('name',)

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ('title', 'image', 'category','text',)
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('comment',)