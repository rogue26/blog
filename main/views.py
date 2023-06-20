from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Blog, Article, Experience


# Create your views here.
class Home(TemplateView):
    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Blog.objects.first()
        context['articles'] = Article.objects.all()
        context['experiences'] = Experience.objects.all()

        return context
