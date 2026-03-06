from django.urls import path
from .views import ArticleListview,ArticleDetailview,ArticleCreateView,ArticleUpdateView

app_name='blog'
urlpatterns = [
    path('',ArticleListview.as_view(),name='article-list'),
    path('detail/<int:pk>', ArticleDetailview.as_view(), name='article-detail'),
    path('update/<int:pk>',ArticleUpdateView.as_view(), name='article-update'),
    path('create', ArticleCreateView.as_view(),name='article_create')
]

