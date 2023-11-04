from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from hexlet_django_blog.article.models import Article

def index(request):
    # return HttpResponse('article')
    return render(request, 'index.html', context={
        'who': 'Articles',
    })


class IndexView(View):

    template_name = 'articles/just_page.html'

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })



def show_tags_id(request, tags, article_id):
    return render(request, 'articles/tags_and_id.html',  context={
        'id': article_id, 'tag': tags
    })


def reversed_view(request):
    reversed_url = reverse('article', args=["gorecode", 17])
    return HttpResponseRedirect(reversed_url)


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })

