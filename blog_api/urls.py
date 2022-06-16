from django.urls import path

from blog_api import views


app_name = 'blog_api'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article-list'),
    path('category/', views.CategoryList.as_view(), name='category-list'),
    path('category/<str:query>/', views.ArticleByCategory.as_view(), name='article-by-category'),

]