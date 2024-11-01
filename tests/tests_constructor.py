from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

class TestConstructor:
    def test_open_constructor_by_clicking_its_button(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_AUTH_FORM).send_keys('olga_semenova_12_666@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_AUTH_FORM).send_keys('567892')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_IN_AUTH_FORM).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_LINK))
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.CONSTRUCT_A_BURGER_LINE))
        assert driver.find_element(*TestLocators.CONSTRUCT_A_BURGER_LINE)

    def test_open_constructor_by_clicking_logo(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_AUTH_FORM).send_keys('olga_semenova_12_666@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_AUTH_FORM).send_keys('567892')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_IN_AUTH_FORM).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_LINK))
        driver.find_element(*TestLocators.STELLAR_BURGERS_LOGO).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.CONSTRUCT_A_BURGER_LINE))
        assert driver.find_element(*TestLocators.CONSTRUCT_A_BURGER_LINE)

    def test_open_sauces_section(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_AUTH_FORM).send_keys('olga_semenova_12_666@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_AUTH_FORM).send_keys('567892')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_IN_AUTH_FORM).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_LINK))
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.CONSTRUCT_A_BURGER_LINE))
        driver.find_element(*TestLocators.SAUCES_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SAUCES_LINE))
        assert driver.find_element(*TestLocators.SAUCES_LINE)

    def test_open_buns_section(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_AUTH_FORM).send_keys('olga_semenova_12_666@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_AUTH_FORM).send_keys('567892')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_IN_AUTH_FORM).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_LINK))
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.CONSTRUCT_A_BURGER_LINE))
        driver.find_element(*TestLocators.SAUCES_BUTTON).click()
        driver.find_element(*TestLocators.BUNS_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.BUNS_LINE))
        assert driver.find_element(*TestLocators.BUNS_LINE)

    def test_open_sauces_section(self, driver):
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.SIGN_IN_FORM))
        driver.find_element(*TestLocators.EMAIL_FIELD_IN_AUTH_FORM).send_keys('olga_semenova_12_666@gmail.com')
        driver.find_element(*TestLocators.PASSWORD_FIELD_IN_AUTH_FORM).send_keys('567892')
        driver.find_element(*TestLocators.SIGN_IN_BUTTON_IN_AUTH_FORM).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(TestLocators.ORDER_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.PROFILE_LINK))
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.CONSTRUCT_A_BURGER_LINE))
        driver.find_element(*TestLocators.FILLINGS_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TestLocators.FILLINGS_LINE))
        assert driver.find_element(*TestLocators.FILLINGS_LINE)



