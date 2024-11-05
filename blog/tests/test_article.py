from typing import Literal
import pytest

# from django.db import IntegrityError
from blog import models


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id,title,author,content,image,publish,status,slug,category,likes,snippet",
    [
        (
            1,
            "Protect or ago trade work.",
            1,
            "Production hospital fish control price. Tend music attorney the eat head network.",
            "media/article_pics/default.png",
            "2022-01-23 01:04:09.060107",
            "draft",
            "admit-marriage-two",
            2,
            [],
            "Allow than bar concern finally why.",
        ),
        (
            2,
            "Late indeed inside wall.",
            1,
            "Myself responsibility cold matter side grow wall. Close local most act nature. Local soon as live.",
            "media/article_pics/default.png",
            "2020-06-02 06:16:24.794596",
            "published",
            "beautiful-civil",
            2,
            [],
            "Inside stop deep white organization choice.",
        ),
    ],
)
def test_blog_article_dbfixture(
    db: None,
    db_fixture_setup: None,
    id: Literal[1, 2],
    title: Literal["Protect or ago trade work.", "Late indeed inside wall."],
    author: Literal[1],
    content: Literal[
        "Production hospital fish control price. Tend music attorney the eat head network.",
        "Myself responsibility cold matter side grow wall. Close local most act nature. Local soon as live.",
    ],
    image: Literal["media/article_pics/default.png"],
    publish: Literal["2022-01-23 01:04:09.060107", "2020-06-02 06:16:24.794596"],
    status: Literal["draft", "published"],
    slug: Literal["admit-marriage-two", "beautiful-civil"],
    category: Literal[2],
    likes: list[int],
    snippet: Literal[
        "Allow than bar concern finally why.",
        "Inside stop deep white organization choice.",
    ],
):
    result = models.Article.objects.get(id=id)
    print(f"result: {result}")
    assert result.title == title
    assert result.author.id == author
    assert result.content == content
    assert result.image == image
    assert result.publish.strftime("%Y-%m-%d %H:%M:%S.%f") == publish
    assert result.status == status
    assert result.slug == slug
    assert result.category.id == category
    assert [like.id for like in result.likes.all()] == likes
    # assert result.likes.id == likes
    assert result.snippet == snippet


def test_blod_db_article_insert_data(
    db: None,
    article_factory,
):
    result = article_factory.create(
        title="title",
        author__id=3,
        content="content",
        image="images/default.png",
        publish="2020-04-09 08:45:11.269818",
        status="published",
        slug="slug",
        category__id=4,
        # likes__id=set(),
        snippet="snippet",
    )
    assert result.title == "title"
    assert result.author.id == 3
    assert result.content == "content"
    assert result.image == "images/default.png"
    assert result.publish == "2020-04-09 08:45:11.269818"
    assert result.status == "published"
    assert result.slug == "slug"
    assert result.category.id == 4
    # assert result.likes.id == set()
    assert result.snippet == "snippet"
