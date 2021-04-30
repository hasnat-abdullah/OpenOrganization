from django.urls import path
from .views import ArticlesListView, ArticleDetailView, CategoryArticlesListView,AuthorArticlesListView

urlpatterns = [
    path('', ArticlesListView.as_view(), name="article_list"),
    path('<int:pk>', ArticleDetailView.as_view(), name="article_details"),
    path('category/<int:pk>', CategoryArticlesListView.as_view(), name="category_articles"),
    path('author/<int:pk>', CategoryArticlesListView.as_view(), name="author_articles"),
]