from model.param_contact import Contact


def test_contact(app):
    app.contact.create(Contact(firstname="Zerg", middle_name="Big", lastname="Fucking",
                               nickname="Koroleva", mesto_raboti="Cosmos", address="hui znaet gde",
                               home_phone="+74958550203",
                               mobile_phone="98801230506", email="zergazaza@mail.ru"))