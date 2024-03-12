from django.urls import path
from .views import ArticleList, ArticleDetail, ArticlePreview, search_view


app_name = 'article'

urlpatterns = [

    path ('', ArticleList.as_view(), name="home"),   
    path ('detail/<slug>', ArticleDetail.as_view(), name='detail'),
    path ('search/', search_view, name='search'),
]









