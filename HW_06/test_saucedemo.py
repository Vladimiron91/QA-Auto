from pages import LoginPage, InventoryPage, CartPage, CheckoutPage, OverviewPage


def test_saucedemo(browser):
    login = LoginPage(browser)
    login.open("https://www.saucedemo.com/")
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(browser)
    inventory.add_products()
    inventory.go_to_cart()

    cart = CartPage(browser)
    cart.checkout()

    checkout = CheckoutPage(browser)
    checkout.fill("Vladimir", "QA", "12345")

    overview = OverviewPage(browser)
    total = overview.get_total()

    assert total == "58.29"