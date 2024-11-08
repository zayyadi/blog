# import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.contrib.sitemaps.views import sitemap
from django.urls import include, path


# from rest_framework.authtoken import views

# import blog.views as blog_views
from blog.sitemaps import PostSitemap

sitemaps = {
    "posts": PostSitemap,
}


urlpatterns = [
    path("admin/", admin.site.urls),
    # path('debug/', include(debug_toolbar.urls)),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', views.obtain_auth_token),
    # path(r'api/auth/', include('knox.urls')),
    path("", include("blog.urls", namespace="blog")),
    # path('api/', include('blog_api.urls', namespace='blog_api')),
    path("users/", include("users.urls", namespace="users")),
    path("summernote/", include("django_summernote.urls")),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("oauth/", include("social_django.urls", namespace="social")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
