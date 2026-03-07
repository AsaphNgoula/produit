from django.urls import path
from .views import List_View,Detail_View

app_name='courses'
urlpatterns = [
    path('',List_View.as_view(),name='courses-list'),
    path('des',List_View.as_view(template_name='courses/courses-list-des.html'),name='courses-des'),
    path('detail/<int:pk>', Detail_View.as_view(), name='course-detail'),
    # path('update/<int:pk>',ArticleUpdateView.as_view(), name='article-update'),
    # path('create', ArticleCreateView.as_view(),name='article_create'),
    # path('delete/<int:pk>',ArticleDeleteView.as_view(), name='article-delete'),

]