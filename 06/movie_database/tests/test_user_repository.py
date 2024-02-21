import pytest
from app import WebApp
from user_repository import UserRepository

@pytest.fixture
def user_repository(request):
    wa = WebApp("sqlite:///test.db")
    wa.init_flask()
    wa.app.app_context().push()
    wa.connect_to_db()
    yield UserRepository(wa.app, wa.db)
    with wa.app.app_context():
        wa.db.drop_all()
    wa.db.session.close()

def test_init(user_repository):
    user = user_repository.by_email_and_password("alexander.stuckenholz@hshl.de", "secret")
    assert user is not None, "User not created"
    assert user.ID == 1, "User.ID not correct"
    assert user.Email == "alexander.stuckenholz@hshl.de", "User.Email not correct"