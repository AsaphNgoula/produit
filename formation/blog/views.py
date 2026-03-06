from django.shortcuts import render,get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.views.generic import ListView,CreateView,DeleteView,DetailView,UpdateView

# Create your views here.
class ArticleCreateView(CreateView):
    form_class =ArticleForm
    template_name='blog/article_create.html'
    queryset=Article.objects.all()
    success_url= '/blog'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    form_class =ArticleForm
    template_name='blog/article_create.html'
    queryset=Article.objects.all()
    success_url='/blog'
    def get_object(self):
        id= self.kwargs.get('pk')
        return get_object_or_404(Article,pk=id)


class ArticleListview(ListView):
    template_name='blog/article_list.html'
    queryset=Article.objects.all()

class ArticleDetailview(DetailView):
    template_name='blog/article_detail.html'

    def get_object(self):
        id= self.kwargs.get('pk')
        return get_object_or_404(Article,pk=id)
    
class ArticleDeleteView(DeleteView):
    template_name='blog/article_Delete.html'
    queryset=Article.objects.all()
    success_url='/blog'