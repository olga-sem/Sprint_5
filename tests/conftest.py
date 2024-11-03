import random
import string
import pytest
from selenium import webdriver
import helpers

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(helpers.URL)
    yield driver
    driver.quit()

@pytest.fixture()
def email():
    letters = random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5)
    email = ''.join(letters) + '@gmail.com'
    return email