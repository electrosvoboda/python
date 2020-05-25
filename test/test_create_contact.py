from model.param_contact import Contact


def test_create_contact(app):
    app.contact.create(Contact(firstname="Zerg", middle_name="Big", lastname="Fucking",
                               nickname="Koroleva", mesto_raboti="Cosmos", address="hui znaet gde",
                               home_phone="+74958550203",
                               mobile_phone="98801230506", email="zergazaza@mail.ru"))


def test_add_new_contact(app):
    app.contact.create(Contact(firstname="ra", middle_name="ss", lastname="ia",
                               nickname="RF", mesto_raboti="Evrazia", address="Its big fucking country",
                               home_phone="112",
                               mobile_phone="02", email="putin@number1.ru"))