import pytest

from blog.models import Comment



@pytest.fixture
def category_with_multiple_children(db):
    record = Comment.objects.build_tree_nodes(
        {
            "id": 1,
            "post": "parent",
            "name": "parent",
            "body": "parent",
            "email": "parent",
            "children": [
                {
                    "id": 2,
                    "parent_id": 1,
                    "name": "child",
                    "slug": "child",
                    "children": [
                        {
                            "id": 3,
                            "parent_id": 2,
                            "name": "grandchild",
                            "slug": "grandchild",
                        }
                    ],
                }
            ],
        }
    )
    category = Comment.objects.bulk_create(record)
    return category