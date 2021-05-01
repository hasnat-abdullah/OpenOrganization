from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.query_utils import Q
from .models import Articles, Category
from logs.log import *


class ArticlesListView(ListView):
    """List view with article name search & pagination"""
    model = Articles
    template_name = 'blog.html'
    context_object_name = 'articles'
    fields = ('title', 'category','author','thumbnail','created_at')
    ordering = '-id'
    paginate_by = 6

    def get_queryset(self):
        query_param = self.request.GET.get("q", None) # get country search query
        if query_param is not None:
            return Articles.objects.filter(Q(title__icontains=query_param)|Q(author__name__icontains=query_param)).order_by('-id')
        return Articles.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(ArticlesListView, self).get_context_data(**kwargs)
        articles = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(articles, self.paginate_by)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        # category
        categories = Category.objects.all().order_by('name')
        context['articles'] = articles
        context['categories'] = categories
        return context


class ArticleDetailView(DetailView):
    """Country details page view"""
    model = Articles
    template_name = 'blog-single.html'
    context_object_name = 'article'


class CategoryArticlesListView(ListView):
    """List view with Article name search & pagination by category"""
    model = Articles
    template_name = 'blog.html'
    context_object_name = 'articles'
    fields = ('title', 'category','author','thumbnail','created_at')
    ordering = '-id'
    paginate_by = 6

    def get_queryset(self):
        query_param = self.request.GET.get("q", None) # get country search query
        if query_param is not None:
            return Articles.objects.filter(Q(title__icontains=query_param) | Q(author__name__icontains=query_param),
                                           category_id=self.kwargs['pk']).order_by('-id')
        return Articles.objects.filter(category_id=self.kwargs['pk']).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(CategoryArticlesListView, self).get_context_data(**kwargs)
        articles = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(articles, self.paginate_by)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        # category
        categories = Category.objects.all().order_by('name')
        context['articles'] = articles
        context['categories'] = categories
        return context


class AuthorArticlesListView(ListView):
    """List view with Article name search & pagination by Author"""
    model = Articles
    template_name = 'blog.html'
    context_object_name = 'articles'
    fields = ('title', 'category','author','thumbnail','created_at')
    ordering = '-id'
    paginate_by = 6

    def get_queryset(self):
        query_param = self.request.GET.get("q", None) # get country search query
        if query_param is not None:
            return Articles.objects.filter(Q(title__icontains=query_param) | Q(author__name__icontains=query_param),
                                           author__id=self.kwargs['pk']).order_by('-id')
        return Articles.objects.filter(author__id=self.kwargs['pk']).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(AuthorArticlesListView, self).get_context_data(**kwargs)
        articles = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(articles, self.paginate_by)
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        # category
        categories = Category.objects.all().order_by('name')
        context['articles'] = articles
        context['categories'] = categories
        return context
