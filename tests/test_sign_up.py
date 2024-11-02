from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators


class TestSignUp:
    def test_sign_up_successfully_new_user(self, driver):
        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.SIGN_UP_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_UP_FORM))
        driver.find_element(*TestLocators.NAME_FIELD).send_keys('Olga')
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys('olga_semennova_12_666@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys('567892')
        driver.find_element(*TestLocators.SIGN_UP_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.SIGN_IN_FORM))
        assert TestLocators.SIGN_IN_FORM

    def test_sign_up_invalid_password(self, driver):
        driver.find_element(*TestLocators.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.SIGN_UP_LINK).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_UP_FORM))
        driver.find_element(*TestLocators.NAME_FIELD).send_keys('Olga')
        driver.find_element(*TestLocators.EMAIL_FIELD).send_keys('olga_semenova_12_666@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_FIELD).send_keys('567')
        driver.find_element(*TestLocators.SIGN_UP_BUTTON).click()
        assert driver.find_element(*TestLocators.INVALID_PASSWORD)






