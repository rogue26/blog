from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    max_home_articles = models.IntegerField()
    github_url = models.CharField(max_length=100)
    linkedin_url = models.CharField(max_length=100)


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    short_desc = models.TextField()
    content = HTMLField()


class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    start_year = models.CharField(max_length=10)
    end_year = models.CharField(max_length=10)
