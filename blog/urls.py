from django.urls import path

from blog import views

from .feeds import AtomSiteNewsFeed, LatestPostsFeed

app_name = "blog"

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("addarticle/", views.addArticle, name="addarticle"),
    path("article/<slug:post>/", views.detail, name="detail"),
    path("update/<slug:slug>", views.updateArticle, name="update"),
    path("approve/<slug:slug>", views.approve_post, name="approve"),
    path("unpub/", views.list_unpublished, name="unpub"),
    path("tag/<slug:slug>/", views.tagged, name="tagged"),
    path("delete/<slug:slug>", views.deleteArticle, name="delete"),
    path("", views.articles, name="articles"),
    path("like/<slug:slug>", views.LikeView, name="article_like"),
    path("add_catergory/", views.addCategory, name="add_category"),
    path("category/<slug:category_slug>", views.category, name="category"),
    path("search/", views.search_posts, name="post_search"),
]
