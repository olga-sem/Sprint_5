from selenium.webdriver.common.by import By


class TestLocators:
    SIGN_IN_BUTTON = [By.XPATH, './/button[text()="Войти в аккаунт"]'] #Кнопка Войти в аккаунт
    SIGN_IN_FORM = [By.XPATH, './/h2[text()="Вход"]'] #Форма входа
    SIGN_UP_LINK = [By.LINK_TEXT, "Зарегистрироваться"] #Ссылка  Зарегистрироваться в форме входа
    SIGN_UP_FORM = [By.XPATH, './/h2[text()="Регистрация"]'] #Форма регистрации
    NAME_FIELD = [By.XPATH, './/fieldset[1]/div/div/input'] #Поле Имя
    EMAIL_FIELD = [By.XPATH, './/fieldset[2]/div/div/input'] #Поле Email
    PASSWORD_FIELD = [By.XPATH, './/input[@name="Пароль"]'] #Поле Пароль
    SIGN_UP_BUTTON = [By.XPATH, './/button[text()="Зарегистрироваться"]'] #Кнопка Зарегистрироваться в форме входа
    INVALID_PASSWORD = [By.XPATH, './/p[text()="Некорректный пароль"]'] #Сообщение Некорректный пароль

    EMAIL_FIELD_IN_AUTH_FORM = [By.XPATH, './/input[@name="name"]'] #Пароль Email в форме регистрации
    PASSWORD_FIELD_IN_AUTH_FORM = [By.XPATH, './/input[@name="Пароль"]'] #Поле Пароль в форме регистрации
    SIGN_IN_BUTTON_IN_AUTH_FORM = [By.XPATH, './/button[text()="Войти"]'] #Кнопка Войти в форме регистрации
    ORDER_BUTTON = [By.XPATH, './/button[text()="Оформить заказ"]'] #Кнопка Оформить заказ
    PERSONAL_ACCOUNT_BUTTON = [By.XPATH,'.//p[text()="Личный Кабинет"]'] #Кнопка Личный кабинет
    SIGN_IN_LINK = [By.XPATH, './/a[text()="Войти"]'] #Ссылка Войти в форме регистрации
    RESET_PASSWORD_LINK = [By.LINK_TEXT, "Восстановить пароль"] #Кнопка Восстановить пароль

    PROFILE_LINK = [By.XPATH, './/a[text()="Профиль"]'] #Кнопка Профиль

    CONSTRUCTOR_BUTTON = [By.XPATH, './/p[text()="Конструктор"]'] #Кнопка Конструктор
    CONSTRUCT_A_BURGER_LINE = [By.XPATH, './/h1[text()="Соберите бургер"]'] #Заголовок Соберите бургер
    STELLAR_BURGERS_LOGO = [By.XPATH, './/div[contains(@class, "AppHeader_header__logo")]'] # Логотип Stellar Burgers
    SAUCES_BUTTON = [By.XPATH, './/span[text()="Соусы"]'] # Кнопка Соусы
    SAUCES_CHOSEN_BUTTON = [By.XPATH, './/div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Соусы"]'] # Кнопка Соусы после таба
    BUNS_BUTTON = [By.XPATH, './/span[text()="Булки"]'] #Кнопка Булки
    BUNS_CHOSEN_BUTTON = [By.XPATH, './/div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Булки"]'] #Кнопка Булки после таба
    FILLINGS_BUTTON = [By.XPATH, './/span[text()="Начинки"]'] #Кнопка Начинки
    FILLINGS_CHOSEN_BUTTON = [By.XPATH, './/div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]/span[text()="Начинки"]'] #Кнопка Начинки после таба

    EXIT_BUTTON = [By.XPATH, './/button[text()="Выход"]'] #Кнопка Выход
