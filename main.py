from symtable import Class

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, ".button.round")
    comfort_rate_icon = (By.XPATH, "//div[@class='tcard-title' and text()='Comfort']")
    phone_number_button = (By.CSS_SELECTOR, ".np-button")
    phone_number_field = (By.ID, "phone")
    next_phone_number_button = (By.CSS_SELECTOR, ".button.full")
    sms_field = (By.ID, "code")
    confirm_sms_number_button = (By.XPATH, "//div[@class='buttons']/button[text()='Confirmar']")
    button_pay_method = (By.CSS_SELECTOR, ".pp-button")
    add_card_number = (By.CSS_SELECTOR, ".pp-plus-container")
    card_number_field = (By.ID, "number")
    add_card_code = (By.NAME, "code")
    add_button = (By.XPATH, "//button[@class='button full' and text()='Agregar']")
    added_card = (By.XPATH, "//div[@class='pp-title' and text()='Tarjeta']")
    payment_method_close = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')
    message_to_driver_field = (By.ID, "comment")
    blanket_and_handkerchief_switch = (By.CLASS_NAME, 'switch')
    blanket_and_handkerchief_input = (By.CLASS_NAME, 'switch-input')
    ice_cream_counter = (By.CLASS_NAME, 'counter-plus')
    order_taxi_button = (By.CSS_SELECTOR, ".smart-button-main")
    close_countdown_modal = (By.XPATH, "//div[contains(@class, 'order-header-time')]")
    trip_details_modal = (By.CLASS_NAME, "order-details")
    driver_name = (By.XPATH, '//div[@class="order-btn-group"][1]/div[2]')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.request_taxi_button)
        )

    def click_on_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_rate_icon(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.comfort_rate_icon)
        )

    def click_on_comfort_rate_icon(self):
        self.get_comfort_rate_icon().click()

    def get_phone_number_button(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.phone_number_button)
        )

    def click_on_phone_number_button(self):
        self.get_phone_number_button().click()

    def get_phone_number_field(self):
        return WebDriverWait(self.driver, 6).until(
            EC.visibility_of_element_located(self.phone_number_field)
        )

    def set_phone_number(self):
        self.get_phone_number_field().send_keys(data.phone_number)

    def get_next_phone_number_button(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.next_phone_number_button)
        )

    def click_on_next_phone_number_button(self):
        self.get_next_phone_number_button().click()

    def get_sms_field(self):
        return WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located(self.sms_field)
        )

    def set_sms_code(self):
        code = retrieve_phone_code(self.driver)
        self.get_sms_field().send_keys(code)

    def get_confirm_sms_number_button(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.confirm_sms_number_button)
        )

    def click_on_confirm_sms_number_button(self):
        self.get_confirm_sms_number_button().click()

    def get_button_pay_method(self):
        return WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self.button_pay_method)
        )

    def click_on_button_pay_method(self):
        self.get_button_pay_method().click()

    def get_add_card_number(self):
        return WebDriverWait(self.driver,5).until(
            EC.element_to_be_clickable(self.add_card_number)
        )

    def click_on_add_card_number(self):
        self.get_add_card_number().click()

    def get_card_number_field(self):
        return WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located(self.card_number_field)
        )

    def set_card_number(self):
        self.get_card_number_field().send_keys(data.card_number)

    def get_add_card_code(self):
        return WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located(self.add_card_code)
        )

    def set_card_code(self):
        self.get_add_card_code().send_keys(data.card_code)

    def get_add_button(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.add_button)
        )

    def click_on_add_button(self):
        self.get_add_button().click()

    def get_added_card(self):
        return WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located(self.added_card)
        )

    def get_payment_method_close(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.payment_method_close)
        )

    def click_on_payment_close_button(self):
        self.get_payment_method_close().click()

    def get_message_to_driver_field(self):
        return WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located(self.message_to_driver_field)
        )

    def set_message_to_driver(self):
        self.get_message_to_driver_field().send_keys(data.message_for_driver)

    def get_blanket_and_handkerchief(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.blanket_and_handkerchief_switch)
        )

    def set_blanket_and_handkerchief_switch(self):
        self.get_blanket_and_handkerchief().click()

    def get_blanket_and_handkerchief_input(self):
        return WebDriverWait(self.driver, 6).until(
            EC.presence_of_element_located(self.blanket_and_handkerchief_input)
        )

    def click_on_blanket_and_handkerchief_input(self):
        self.get_blanket_and_handkerchief_input().click()

    def get_ice_cream_counter(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.ice_cream_counter)
        )

    def click_ice_cream_counter(self):
        self.get_ice_cream_counter().click()

    def get_counter_value(self):  # Se obtiene el valor inicial del contador
        counter_element = self.driver.find_element(By.CLASS_NAME, "counter-value")
        return int(counter_element.text)

    def get_order_taxi_button(self):
        return WebDriverWait(self.driver, 6).until(
            EC.element_to_be_clickable(self.order_taxi_button)
        )

    def click_on_order_taxi_button(self):
        self.get_order_taxi_button().click()

    def wait_close_countdown_modal(self):
        WebDriverWait(self.driver, 60).until(
            EC.invisibility_of_element_located(UrbanRoutesPage.close_countdown_modal)
        )

    def get_driver_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.driver_name)
        )

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_select_comfort_rate_icon(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_request_taxi_button()
        routes_page.click_on_comfort_rate_icon()
        comfort_rate = routes_page.get_comfort_rate_icon().text
        comfort_text = "Comfort"
        assert comfort_text in comfort_rate

    def test_enter_phone_number(self):
        self.test_select_comfort_rate_icon()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_phone_number_button()
        routes_page.set_phone_number()
        assert data.phone_number == routes_page.get_phone_number_field().get_property("value")

        routes_page.click_on_next_phone_number_button()
        routes_page.set_sms_code()
        routes_page.click_on_confirm_sms_number_button()
        assert routes_page.get_phone_number_button().text == data.phone_number

    def test_enter_payment_method(self):
        self.test_enter_phone_number()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_button_pay_method()
        routes_page.click_on_add_card_number()
        routes_page.set_card_number()
        routes_page.get_card_number_field().send_keys(Keys.TAB)
        routes_page.set_card_code()
        routes_page.get_add_button().send_keys(Keys.TAB)
        routes_page.click_on_add_button()
        routes_page.click_on_payment_close_button()
        assert routes_page.get_added_card().text == 'Tarjeta'

    def test_enter_message_to_driver(self):
        self.test_enter_payment_method()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.get_message_to_driver_field().send_keys(Keys.TAB)
        routes_page.set_message_to_driver()
        assert data.message_for_driver == routes_page.get_message_to_driver_field().get_attribute("value")

    def test_select_blanket_and_handkerchief(self):
        self.test_enter_message_to_driver()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_blanket_and_handkerchief_switch()
        assert routes_page.get_blanket_and_handkerchief_input().get_property('checked')  # Aquí se confirma que el switch está activado

    def test_add_ice_cream(self):
        self.test_select_blanket_and_handkerchief()
        routes_page = UrbanRoutesPage(self.driver)
        initial_value = routes_page.get_counter_value()
        routes_page.click_ice_cream_counter()
        new_value = routes_page.get_counter_value()
        assert new_value == initial_value + 1, f"Error: Se esperaba {initial_value + 1}, resultado {new_value}"  # Aquí se confirma que el contador aumentó en 1

    def test_order_taxi_button(self):
        self.test_add_ice_cream()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_request_taxi_button()

    def test_trip_details_modal_after_countdown(self):
        self.test_order_taxi_button()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_close_countdown_modal()
        driver_name = routes_page.get_driver_name().text
        assert driver_name != "", f"El nombre del conductor no debería estar vacío, resutado: '{driver_name}'"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
