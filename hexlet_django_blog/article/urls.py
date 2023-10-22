from django.urls import path

from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import JustStaticPage

urlpatterns = [
    # path('', views.index),
    path('', JustStaticPage.as_view(template_name = "articles/index.html")),
    # path('', TemplateView.as_view(template_name='index.html')),

]