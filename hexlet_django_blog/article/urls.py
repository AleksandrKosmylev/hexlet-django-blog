from django.urls import path

from hexlet_django_blog.article import views
# from hexlet_django_blog.article.views import JustDynamicPage
from hexlet_django_blog.article.views import IndexView, ArticleView
# from hexlet_django_blog.article.views import ArticleView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('index', views.index),
    path('', IndexView.as_view()),
    # path('', JustStaticPage.as_view(template_name='index.html')),
    # path('', JustStaticPage.as_view(template_name = "articles/index.html")),
    path('ogo', TemplateView.as_view(template_name='articles/index.html')),
    path('<str:tags>/<int:article_id>', views.show_tags_id),
    path('<str:tags>/<int:article_id>', IndexView.as_view(), name='article'),
    path('<int:id>/', ArticleView.as_view(), name='article_link'),
]
