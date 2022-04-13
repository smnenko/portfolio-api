import logging
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from fake_useragent import UserAgent
from webdriver_manager.firefox import GeckoDriverManager

from apps.core.utils.human_util import FakeHuman

logging.basicConfig(level=logging.INFO)


class WebDriver:

    def __init__(self):
        self.user_agent = UserAgent().random
        options = Options()
        self._configure_user_agent(options, self.user_agent)
        self.driver = webdriver.Firefox(
            service=(
                Service(
                    GeckoDriverManager().install(),
                    log_path=Path().resolve().parent.parent.parent.joinpath('geckodriver.log')
                )
            ),
            options=options
        )

    @staticmethod
    def _configure_user_agent(options: Options, user_agent: str):
        options.set_preference('general.useragent.override', user_agent)

    def get_driver(self):
        return self.driver


class MailCreationUtil:

    URL = (
        'https://id.rambler.ru/login-20/mail-registration'
        '?=undefined&rname=mail&theme=&session=false'
        '&back=https%3A%2F%2Fmail.rambler.ru%2F&param=embed&iframeOrigin=https%3A%2F%2Fmail.rambler.ru'
    )

    # https://id.rambler.ru/login-20/mail-registration?=undefined&rname=mail&theme=&session=false&back=https%3A%2F%2Fmail.rambler.ru%2F&param=embed&iframeOrigin=https%3A%2F%2Fmail.rambler.ru

    def __init__(self):
        self.HUMAN = FakeHuman()
        self.username = self.HUMAN.username
        self.password = self.HUMAN.password
        self.secret = self.HUMAN.secret_answer
        self.DRIVER = WebDriver().get_driver()
        self.form = None

    def _fill_username_field(self):
        login = self.form.find_element(By.ID, 'login')
        login.click()
        login.send_keys(self.username)

    def _fill_password_field(self):
        password = self.form.find_element(By.ID, 'newPassword')
        password.click()
        password.send_keys(self.password)
        password_confirm = self.form.find_element(By.ID, 'confirmPassword')
        password_confirm.click()
        password_confirm.send_keys(self.password)

    def _fill_secret_field(self):
        question_input = self.form.find_element(
            By.XPATH,
            '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/form/section[4]/div/div/div[1]/div/div/div/input'
        )
        question_input.click()
        questions_selector = self.form.find_element(By.CLASS_NAME, 'rui-RelativeOverlay-content')
        try:
            question_options = (
                questions_selector
                .find_element(By.CLASS_NAME, 'rui-Menu-content')
                .find_elements(By.TAG_NAME, 'div')
            )
            for el in question_options:
                if el.text == 'Четыре последние цифры кредитной карты':
                    el.click()
        except StaleElementReferenceException:
            logging.info('The element from selector has been chosen and DIV has been deleted')

        question_answer = self.form.find_element(By.ID, 'answer')
        question_answer.click()
        question_answer.send_keys(self.HUMAN.secret_answer)

    def _get_captcha_img(self):
        return (
            self.form
            .find_element(
                By.XPATH,
                '/html/body/div[1]/div/div/div[2]/div/div/div/div[1]/form/section[6]/div/div/div[1]/img'
            ).get_attribute('src')
        )

    def _fill_captcha_field(self, answer: str):
        captcha_input = self.form.find_element(By.NAME, 'recaptcha')
        captcha_input.click()
        captcha_input.send_keys(answer)

    def _approve_account(self):
        elem = (By.LINK_TEXT, 'Добавить позже')
        try:
            wait = WebDriverWait(self.DRIVER, 15)
            wait.until(EC.presence_of_element_located(elem))
            wait.until(EC.element_to_be_clickable(elem))
            self.DRIVER.find_element(elem[0], elem[1]).click()
        except Exception:
            raise TimeoutError

    def create_account(self):
        self.DRIVER.get(self.URL)
        self.form = self.DRIVER.find_element(By.TAG_NAME, 'form')
        self._fill_username_field()
        self._fill_password_field()
        self._fill_secret_field()

        answer = yield self._get_captcha_img()

        self._fill_captcha_field(answer)
        self.form.submit()
        self._approve_account()
        self.DRIVER.quit()
        return f'{self.HUMAN.username}@rambler.ru', self.HUMAN.password, self.HUMAN.secret_answer


if __name__ == '__main__':
    ma = MailCreationUtil()
    g = ma.create_account()
    captcha_img = g.send(None)
    captcha_answer = input(f'{captcha_img}\n!> ')
    try:
        something = g.send(captcha_answer)
    except StopIteration as e:
        print(e)
