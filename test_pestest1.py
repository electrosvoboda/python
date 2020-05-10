from group import Group
from application import Application
import pytest

from param_contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="huiz", header="sobaka", footer="wtf"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()


def test_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="Zerg", middle_name="Big", lastname="Fucking",
                                   nickname="Koroleva", mesto_raboti="Cosmos", address="hui znaet gde",
                                   home_phone="+74958550203",
                                   mobile_phone="98801230506", email="zergazaza@mail.ru"))
    app.logout()