from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators
import data_for_tests


class TestSignUp:
    def test_sign_up_successfully_new_user(self, driver, email):
        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.SIGN_UP_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_UP_FORM))
        driver.find_element(*TestLocators.NAME_FIELD).send_keys(data_for_tests.name)
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(data_for_tests.password)
        driver.find_element(*TestLocators.SIGN_UP_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.SIGN_IN_FORM))
        assert TestLocators.SIGN_IN_FORM

    def test_sign_up_invalid_password(self, driver, email):
        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.SIGN_UP_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_UP_FORM))
        driver.find_element(*TestLocators.NAME_FIELD).send_keys(data_for_tests.name)
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys(data_for_tests.password)
        driver.find_element(*TestLocators.SIGN_UP_BUTTON).click()
        assert driver.find_element(*TestLocators.INVALID_PASSWORD)






