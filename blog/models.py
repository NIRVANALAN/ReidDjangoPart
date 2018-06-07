from django.db import models
from django import forms


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)


class BlogPost_toForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('timestamp',)


class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea(attrs={'row":3' 'cols': 60}))
    timestamp = forms.DateTimeField()


class DiaryPost(models.Model):
    title = models.CharField(max_length=30)
    participants = models.CharField(max_length=50)
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)
