import pytest
from django.core.management import call_command


@pytest.fixture(scope="session")
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load DB data fixtures
    """
    with django_db_blocker.unblock():
        call_command("loaddata", "category_data.json")
        call_command("loaddata", "users_data.json")
        call_command("loaddata", "article_data.json")
