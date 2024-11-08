import os

from uuid import uuid4

from ourblog import settings
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

# from users.models import CustomUser


from django_summernote.fields import SummernoteTextField
from mptt.models import MPTTModel, TreeForeignKey
from PIL import Image
from taggit.managers import TaggableManager


def path_and_rename(instance, filename):
    upload_to = "article_pics"
    ext = filename.split(".")[-1]
    # get filename
    if instance.pk:
        filename = "{}.{}".format(instance.pk, ext)
    else:
        # set filename as random string
        filename = "{}.{}".format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse("blog:category", args=[self.slug])

    def __str__(self):
        return self.name


class Article(models.Model):

    class UnpublishedManager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset().filter(status="draft")

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status="published")

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=150)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    content = SummernoteTextField()
    image = models.ImageField(upload_to=path_and_rename, default="article/default.jpg")
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=options, default="draft")
    slug = models.SlugField(unique=True, max_length=100)
    tags = TaggableManager()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="likes",
    )
    objects = models.Manager()
    unpublished = UnpublishedManager()
    snippet = models.CharField(max_length=255)

    def total_likes(self):
        return self.likes.count()

    class Meta:
        permissions = [
            ("can_publish", "Can publish posts"),
            ("can_edit", "Can edit posts"),
            ("can_view", "Can view posts"),
        ]
        ordering = ["-publish"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("blog:detail", args=[self.slug])

    def get_tags(self):
        """names() is a django-taggit method, returning a ValuesListQuerySet
        (basically just an iterable) containing the name of each tag as a string
        """
        return self.tags.names()

    def get_comments(self):
        return self.comments.filter(parent=None).filter(active=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Article, self).save(*args, **kwargs)


class Comment(MPTTModel):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    name = models.CharField(max_length=50, null=True)
    body = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    email = models.EmailField(default="wk@example.com")

    class MPTTMeta:
        order_insertion_by = ["publish"]

    # def get_comments(self):
    #     """Retrieve only active comments that are direct replies to this comment."""
    #     return self.get_children().filter(active=True)

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


LIKE_CHOICES = (
    ("Like", "Like"),
    ("Unlike", "Unlike"),
)
