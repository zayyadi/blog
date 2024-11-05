import factory
import pytest
from faker import Faker
from pytest_factoryboy import register
from django.utils import timezone

from blog.models import Category, Article
from ourblog.settings import AUTH_USER_MODEL as User

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "cat_slug_%d" % n)
    slug = fake.lexify(text="cat_slug_??????")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Sequence(lambda n: f"user_{n}")
    last_name = factory.Sequence(lambda n: f"last_{n}")
    email = factory.LazyAttribute(lambda obj: f"{obj.first_name}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "password")


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Sequence(lambda n: f"Article {n}")
    author = factory.SubFactory(UserFactory)
    content = factory.Faker("text")
    image = factory.django.ImageField(from_path="path/to/default/image.jpg")
    publish = factory.Faker(
        "date_time_this_decade", tzinfo=timezone.get_current_timezone()
    )
    status = factory.Iterator(["draft", "published"])
    slug = factory.Sequence(lambda n: f"article-{n}")
    tags = factory.Faker("words", nb=3)
    category = factory.SubFactory(CategoryFactory)
    snippet = factory.Faker("text", max_nb_chars=255)


register(CategoryFactory)
register(UserFactory)
register(ArticleFactory)
