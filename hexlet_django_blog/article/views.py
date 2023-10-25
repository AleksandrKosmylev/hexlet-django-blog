from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

def index(request):
    return HttpResponse('article')


"""
def index(request):
    return render(request, 'index.html', context={
        'who': 'Articles',
    })
"""


class JustStaticPage(View):

    template_name = 'articles/just_page.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, class IndexView(View)!')



def show_tags_id(request, tags, article_id):
    return render(request, 'tags_and_id.html',  context={
        'id': article_id, 'tag': tags
    })

def reversed_view(request):
    reversed_url = reverse('article', args=["gorecode", 17])
    return HttpResponseRedirect(reversed_url)