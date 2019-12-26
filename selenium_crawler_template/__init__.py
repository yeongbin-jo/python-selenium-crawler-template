from functools import wraps

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Crawler(object):
    def __init__(self, headless=True, window_size='1920,1080', additional_options=[], timeout=3):
        options = Options()
        options.headless = headless
        if window_size:
            options.add_argument(f'--window-size={window_size}')
        for o in additional_options:
            options.add_argument(o)
        self.driver = webdriver.Chrome(options=options)
        self.timeout = timeout
        self.driver.implicitly_wait(self.timeout)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def close(self):
        """Quit selenium driver"""
        self.driver.quit()

    def _scroll_to_body_bottom(self):
        """Move scroll to bottom of page(document.body)"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def _scroll_to(self, height):
        """
        Set `scrollTop` of `document.scrollingElement`

        :param height: A height to set
        :return:
        """
        self.driver.execute_script(f"document.scrollingElement.scrollTop = '{height}';")

    @staticmethod
    def open_url_in_new_tab(func):
        """
        With this decorator, the first argument of the function opens in a new tab of the browser.

        :param func: A function to use decorator
        :return:
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            self = args[0]
            url = args[1]
            current_handle_index = self.driver.window_handles.index(self.driver.current_window_handle)
            self.driver.execute_script(f'window.open("{url}", "_blank")')
            self.driver.switch_to.window(self.driver.window_handles[-1])
            result = func(*args, **kwargs)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[current_handle_index])
            return result

        return wrapper

    def find_element(self, css_selector, from_element=None, timeout=3):
        """Find dom element via CSS selector w/o NoSuchElementException"""
        if not from_element:
            from_element = self.driver
        self.driver.implicitly_wait(timeout)
        ele = None
        try:
            ele = from_element.find_element(By.CSS_SELECTOR, css_selector)
        except NoSuchElementException:
            pass
        self.driver.implicitly_wait(self.timeout)
        return ele

    def find_elements(self, css_selector, from_element=None, timeout=3):
        """Find dom elements via CSS selector w/o NoSuchElementException"""
        if not from_element:
            from_element = self.driver
        self.driver.implicitly_wait(timeout)
        eles = []
        try:
            eles = from_element.find_elements(By.CSS_SELECTOR, css_selector)
        except NoSuchElementException:
            pass
        self.driver.implicitly_wait(self.timeout)
        return eles

    def resolve_alert(self):
        """Accept alert regardless of existence"""
        try:
            self.driver.switch_to.alert.accept()
        except NoAlertPresentException:
            pass

    def click_action(self, element, offset_x=3, offset_y=3):
        """Action for clicking location of element"""
        ac = ActionChains(self.driver)
        ac.move_to_element(element).move_by_offset(offset_x, offset_y).click().perform()

    def crawl(self, **kwargs):
        """
        Crawling method

        :return:
        """
        raise NotImplementedError()
