from typing import Any
from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.views.generic import ListView, DetailView




class ArticleList(ListView):
 
    global queryset
    # delcaring queryset global to avoid repeating the query 
    # model = Article
    template_name = 'blog/home.html'
    context_object_name = 'articles'
    queryset = Article.objects.published()
    
    def get_context_data(self, **kwargs):
        '''for displaying recent posts'''

        context = super().get_context_data(**kwargs)
        context['recent'] = queryset[:7]
        return context 


class ArticleDetail(DetailView):
   
    model = Article
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)
    

class ArticlePreview(DetailView):
   
    model = Article
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)




class CategoryList(ListView):
    
    model = Category
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = category
        return context



   
