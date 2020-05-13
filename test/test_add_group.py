from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="huiz", header="sobaka", footer="wtf"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
