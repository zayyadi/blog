from django.urls import path

from blog_api.api import RegistrationAPI, LoginAPI, UserAPI
from blog_api import views

from knox.views import LogoutView


app_name = 'blog_api'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='article-list'),
    path('create/', views.CreateArticle.as_view(), name='create-article'),
    path('detail/<slug:slug>', views.ArticleDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', views.DeleteArticle.as_view(), name='delete-article'),
    path('edit/<int:pk>', views.EditArticle.as_view(), name='edit-article'),
    path('search/', views.ArticleListDetailfilter.as_view(), name='search'),
    path('category/', views.CategoryList.as_view(), name='category-list'),
    path('category/<str:query>/', views.ArticleByCategory.as_view(), name='article-by-category'),
    path('comment/', views.CommentView.as_view(), name='comment'),
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('user/', UserAPI.as_view()),
    path('logout/', LogoutView.as_view(), name='knox_logout'),

]