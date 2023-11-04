from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from hexlet_django_blog.article.models import Article


"""
def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })
"""


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, from IndexView(View)')


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['who'] = '(from HomePageView(TemplateView))'
        return context
    """
    #  comes from articles.url (uses reverse)
    def get(self, request, *args, **kwargs):
        reversed_url = reverse('article', args=["python", 42])
        return HttpResponseRedirect(reversed_url)
    """

def about(request):
    return render(request, 'about.html')

