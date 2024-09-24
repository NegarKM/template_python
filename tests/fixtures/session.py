import pytest
from sqlalchemy.orm import sessionmaker

from tests.database import init_test_db


@pytest.fixture
def db_session():
    return sessionmaker()(bind=init_test_db.db_engine)
