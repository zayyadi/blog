import pytest
from django.db import IntegrityError
from blog import models


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug",
    [
        (1, "Name-1", "xfwur"),
        (2, "Name-2", "fgkpu"),
    ],
)
def test_blog_category_dbfixture(
    db,
    db_fixture_setup,
    id,
    name,
    slug,
):
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug


@pytest.mark.parametrize(
    "name, slug",
    [
        ("fashion", "fashion"),
        ("trainers", "trainers"),
        ("baseball", "baseball"),
    ],
)
def test_blog_db_category_insert_data(db, category_factory, name, slug):
    result = category_factory.create(
        name=name,
        slug=slug,
    )
    assert result.name == name
    assert result.slug == slug
