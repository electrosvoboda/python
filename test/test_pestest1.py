from model.group import Group
from fixture.application import Application
import pytest

from model.param_contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="huiz", header="sobaka", footer="wtf"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()


def test_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="Zerg", middle_name="Big", lastname="Fucking",
                                   nickname="Koroleva", mesto_raboti="Cosmos", address="hui znaet gde",
                                   home_phone="+74958550203",
                                   mobile_phone="98801230506", email="zergazaza@mail.ru"))
    app.session.logout()