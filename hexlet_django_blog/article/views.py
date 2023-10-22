from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
"""
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


"""
class JustStaticPage(TemplateView):
    # template_name = "articles/index.html"
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = '(JustStaticPage(TemplateView)))'
        return context

