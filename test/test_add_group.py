from model.group import Group
from model.param_contact import Contact


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="huiz", header="sobaka", footer="wtf"))
    app.session.logout()
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
    app.session.logout()
