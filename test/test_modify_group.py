from model.group import Group


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="azaza"))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="azaza", header="wahwah"))
    app.group.modify_first_group(Group(header="New header"))