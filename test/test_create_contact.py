from model.contact import Contact


def test_create_contact(app):
    app.contact.create(Contact(firstname="Zerg", lastname="Fucking", homephone="+74958550203",
                               mobilephone="98801230506", workphone="+74958451213"))


def test_add_new_contact(app):
    app.contact.create(Contact(firstname="ra", lastname="ia", homephone="112",
                               mobilephone="02", workphone="111"))