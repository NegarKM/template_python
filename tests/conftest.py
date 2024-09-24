import pytest
from sqlalchemy.orm import sessionmaker

# isort: off
# fmt: off
# this needs to be before api_service.models imports
from tests.database import init_test_db

from api_service.models.db_models.user import DBUser as User
# fmt: on
# isort: on

MODELS = [
    User,
]


def _cleanup_tables(session, tables):
    for table in tables:
        rows = session.query(table).all()
        for row in rows:
            session.delete(row)
    session.commit()


@pytest.fixture(scope="function", autouse=True)
def teardown():
    db_session = sessionmaker()(bind=init_test_db.db_engine)
    _cleanup_tables(db_session, MODELS)
