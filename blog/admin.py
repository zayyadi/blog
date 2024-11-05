from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from mptt.admin import MPTTModelAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# from import_export import resources
# from import_export.admin import ImportExportModelAdmin

from .models import Article, Category, Comment


class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "author", "status", "publish")
    list_filter = ("status", "publish")
    search_fields = ["title", "content"]

    summernote_fields = ("content",)


@admin.register(Article)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "status", "slug", "author")
    prepopulated_fields = {
        "slug": ("title",),
    }


class ArticleResources(resources.ModelResource):
    class Meta:
        model = Article


class CategoryResources(resources.ModelResource):
    class Meta:
        model = Category


class CommentResources(resources.ModelResource):
    class Meta:
        model = Comment


# class PostInline


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('author', 'body', 'post', 'created_on', 'active')
#     list_filter = ('active', 'created_on')
#     search_fields = ('author', 'email', 'body')
#     actions = ['approve_comments']

#     def approve_comments(self, request, queryset):
#         queryset.update(active=True)


# admin.site.register(Article, ImportExportModelAdmin)
admin.site.register(Category, ImportExportModelAdmin)
admin.site.register(Comment, MPTTModelAdmin)
