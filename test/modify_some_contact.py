from model.contact import Contact


def modify_contact(app):
    if app.contact.count == 0:
        app.contact.create(Contact(firstname="Huerg"))

