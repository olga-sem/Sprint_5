from selenium.webdriver.common.by import By


class TestLocators:
    SIGN_IN_BUTTON = [By.XPATH, '//*[contains(@class, "button_button")]'] #Кнопка Войти в аккаунт
    SIGN_IN_FORM = [By.XPATH, '//*[contains(@class, "Auth_login")]'] #Форма входа
    SIGN_UP_BUTTON = [By.XPATH, '//*[contains(@class, "Auth_link") and text() = "Зарегистрироваться"]'] #Кнопка Зарегистрироваться в форме входа
    SIGN_UP_FORM = [By.XPATH, '//*[contains(@class, "App_componentContainer")]'] #Форма регистрации
    NAME_FIELD = [By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'] #Поле Имя
    EMAIL_FIELD = [By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'] #Поле Email
    PASSWORD_FIELD = [By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input'] #Поле Пароль
    SIGN_UP_NEW_BUTTON = [By.XPATH, '//*[contains(@class, "button") and text() = "Зарегистрироваться"]'] #Кнопка Зарегистрироваться в форме регистрации
    INVALID_PASSWORD = [By.XPATH, '//*[contains(@class, "input__error text_type_main-default")]'] #Сообщение Некорректный пароль

    EMAIL_FIELD_IN_AUTH_FORM = [By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'] #Пароль Email в форме регистрации
    PASSWORD_FIELD_IN_AUTH_FORM = [By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'] #Поле Пароль в форме регистрации
    SIGN_IN_BUTTON_IN_AUTH_FORM = [By.XPATH, '//*[contains(@class, "button_button") and text()="Войти"]'] #Кнопка Войти в форме регистрации
    ORDER_BUTTON = [By.XPATH, '//*[contains(@class, "button_button") and text()="Оформить заказ"]'] #Кнопка Оформить заказ
    PERSONAL_ACCOUNT_BUTTON = [By.XPATH,'//*[contains(@class, "AppHeader_header__linkText") and text()="Личный Кабинет"]'] #Кнопка Личный кабинет
    SIGN_IN_LINK = [By.XPATH, '//*[contains(@class, "Auth_link") and text()="Войти"]'] #Кнопка Войти в окне Личный кабинет
    RESET_PASSWORD_LINK = [By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a'] #Кнопка Восстановить пароль
    RESET_PASSWORD_LINE = [By.XPATH, '//*[@id="root"]/div/main/div/h2'] #Заголовок Восстановить пароль

    PROFILE_LINK = [By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[1]/a'] #Кнопка Профиль

    CONSTRUCTOR_BUTTON = [By.XPATH, '//*[contains(@class, "AppHeader_header__linkText") and text()="Конструктор"]'] #Кнопка Конструктор
    CONSTRUCT_A_BURGER_LINE = [By.XPATH, '//*[@id="root"]/div/main/section[1]/h1'] #Заголовок Соберите бургер
    STELLAR_BURGERS_LOGO = [By.XPATH, '//*[@id="root"]/div/header/nav/div/a'] # Логотип Stellar Burgers
    SAUCES_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]'] # Кнопка Соусы
    SAUCES_LINE = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]'] # Заголовок Соусы
    BUNS_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]'] #Кнопка Булки
    BUNS_LINE = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]'] #Заголовок Булки
    FILLINGS_BUTTON = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]'] #Кнопка Начинки
    FILLINGS_LINE = [By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]'] #Заголовок Начинки

    EXIT_BUTTON = [By.XPATH, '//*[contains(@class, "Account_button") and text()="Выход"]'] #Кнопка Выход
