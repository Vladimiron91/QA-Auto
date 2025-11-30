from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def send(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def text(self, locator):
        return self.driver.find_element(*locator).text


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def login(self, username, password):
        self.send(self.USERNAME, username)
        self.send(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)


class InventoryPage(BasePage):
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART = (By.CLASS_NAME, "shopping_cart_link")

    def add_products(self):
        self.click(self.BACKPACK)
        self.click(self.TSHIRT)
        self.click(self.ONESIE)

    def go_to_cart(self):
        self.click(self.CART)


class CartPage(BasePage):
    CHECKOUT = (By.ID, "checkout")

    def checkout(self):
        self.click(self.CHECKOUT)


class CheckoutPage(BasePage):
    FIRST = (By.ID, "first-name")
    LAST = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")

    def fill(self, first, last, zip_code):
        self.send(self.FIRST, first)
        self.send(self.LAST, last)
        self.send(self.ZIP, zip_code)
        self.click(self.CONTINUE)


class OverviewPage(BasePage):
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def get_total(self):
        raw = self.text(self.TOTAL)   # "Total: $58.29"
        return raw.replace("Total: $", "").strip()