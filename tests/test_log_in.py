from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators


class TestSignIn:
    def test_sign_in_with_button_log_in_an_account(self, driver):
        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_AUTH_FORM).send_keys('olga_semenova_12_666@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_AUTH_FORM).send_keys('567892')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_IN_AUTH_FORM).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert driver.find_element(*TestLocators.ORDER_BUTTON)

    def test_sign_in_with_personal_account_button(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_AUTH_FORM).send_keys('olga_semenova_12_666@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_AUTH_FORM).send_keys('567892')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_IN_AUTH_FORM).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert driver.find_element(*TestLocators.ORDER_BUTTON)

    def test_sign_in_with_log_in_button_in_auth_form(self, driver):
        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.SIGN_UP_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_UP_FORM))
        driver.find_element(*TestLocators.SIGN_IN_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_AUTH_FORM).send_keys('olga_semenova_12_666@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_AUTH_FORM).send_keys('567892')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_IN_AUTH_FORM).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert driver.find_element(*TestLocators.ORDER_BUTTON)

    def test_sign_in_with_reset_password_link(self, driver):
        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.RESET_PASSWORD_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_LINK))
        driver.find_element(*TestLocators.SIGN_IN_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_AUTH_FORM).send_keys('olga_semenova_12_666@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_AUTH_FORM).send_keys('567892')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_IN_AUTH_FORM).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        assert driver.find_element(*TestLocators.ORDER_BUTTON)





