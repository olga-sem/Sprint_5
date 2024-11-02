from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

class TestLogOut:
    def test_log_out_with_exit_button(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_AUTH_FORM).send_keys('olga_semenova_12_666@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_AUTH_FORM).send_keys('567892')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_IN_AUTH_FORM).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_LINK))
        driver.find_element(*TestLocators.EXIT_BUTTON)
        assert TestLocators.SIGN_IN_FORM
