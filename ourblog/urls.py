import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import TemplateView

import blog.views as blog_views
from blog.sitemaps import PostSitemap

from .views import home, send_push

sitemaps = {
    "posts": PostSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('debug/', include(debug_toolbar.urls)),
    path('', include('blog.urls', namespace='blog')),
    path('summernote/', include('django_summernote.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path('settings/', blog_views.settings, name='settings'),
    path('settings/password/', blog_views.password, name='password'),
    path('home', home),
    path('register/', blog_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('send_push', send_push),
    path('webpush/', include('webpush.urls')),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
