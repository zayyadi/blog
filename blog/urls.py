
from django.urls import path

from blog import views
from .feeds import LatestPostsFeed, AtomSiteNewsFeed
from blog.views import AddCategoryView
app_name = 'blog'

urlpatterns=[
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path('dashboard/',views.dashboard,name = "dashboard"),
    path('addarticle/',views.addArticle,name = "addarticle"),
    path('article/<slug:post>/',views.detail,name = "detail"),
    path('update/<slug:slug>',views.updateArticle,name = "update"),
    path('tag/<slug:tag_slug>/', views.articles, name="article_tag"),
    path('delete/<slug:slug>',views.deleteArticle,name = "delete"),
    path('',views.articles,name = "articles"),
    path('like/<slug:slug>', views.LikeView, name="article_like"),
    path('add_catergory/', AddCategoryView.as_view(), name="add_category"),
    path('category/<str:category>/', views.CategoryView, name='category'),
    path('profile/', views.profile, name='profile'), 
]