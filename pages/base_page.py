import logging
from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

ANIMATION_PAUSE_TIME = 1


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def current_url(self):
        return self.driver.current_url

    def _clear(self, locator):
        self._find_clickable_element(locator).clear()

    def _clear_input(self, locator):
        element = self._find_visible_element(locator)

        while len(element.get_attribute('value')) > 0:
            element.send_keys(Keys.BACKSPACE)

    def _click(self, locator):
        self._find_clickable_element(locator).click()

    def _click_with_javascript(self, locator=None, element=None):
        if element:
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element = self._find_clickable_element(locator)
            self.driver.execute_script("arguments[0].click();", element)

    def _find_clickable_element(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(expected_conditions.element_to_be_clickable((locator['by'], locator['value'])))
        except TimeoutException:
            return None

    def _find(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def _find_many(self, locator):
        return self.driver.find_elements(locator['by'], locator['value'])

    def _find_present_element(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(expected_conditions.presence_of_element_located((locator['by'], locator['value'])))
        except TimeoutException:
            return None

    def _find_present_elements(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(expected_conditions.presence_of_all_elements_located((locator['by'], locator['value'])))
        except TimeoutException:
            return []

    def _find_visible_element(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(expected_conditions.visibility_of_element_located((locator['by'], locator['value'])))
        except TimeoutException:
            return None

    def _find_visible_elements(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(expected_conditions.visibility_of_all_elements_located((locator['by'], locator['value'])))
        except TimeoutException:
            return []

    def _get_attribute_from_element(self, locator, attribute_name, timeout=10):
        element = self._find_present_element(locator, timeout)

        return element.get_attribute(attribute_name)

    def _get_text_from_element(self, locator, split_and_join=True, strip=True, timeout=10):
        element_text = self._find_visible_element(locator, timeout).text

        if split_and_join:
            element_text = " ".join(element_text.split())

        if strip:
            element_text = element_text.strip()

        return element_text

    def _get_text_from_elements(self, locator, timeout=10):
        elements = self._find_present_elements(locator, timeout)

        return [' '.join(element.text.split()).strip() for element in elements]

    def _get_inner_text_from_elements(self, locator, timeout=10):
        elements = self._find_present_elements(locator, timeout)

        return [' '.join(element.get_attribute('innerText').split()).strip() for element in elements]

    def _is_displayed(self, locator, timeout=0):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(expected_conditions.visibility_of_element_located((locator['by'], locator['value'])))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._find(locator).is_displayed()
            except NoSuchElementException:
                return False

    def _is_not_displayed(self, locator, timeout=0):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(expected_conditions.invisibility_of_element_located((locator['by'], locator['value'])))
        except TimeoutException:
            return False
        return True

    def _is_present(self, locator, timeout=0):
        if timeout > 0:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(expected_conditions.presence_of_element_located((locator['by'], locator['value'])))
            except TimeoutException:
                return False
            return True
        else:
            try:
                return self._find(locator).is_displayed()
            except NoSuchElementException:
                return False

    def _move_to_element(self, locator=None, element=None):
        if element:
            ActionChains(self.driver).move_to_element(element).perform()
        else:
            ActionChains(self.driver).move_to_element(self._find_present_element(locator)).perform()

    def _pause_for_animation(self, pause_time=1):
        logging.info(f'Pausing for animation for {pause_time} second{"s" if pause_time > 1 else ""}.')
        sleep(pause_time)

    def _press_enter_key(self, locator):
        self._type(locator, Keys.ENTER)

    def _press_escape_key(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

    def _refresh_page(self):
        self.driver.refresh()

    def _scroll_to_bottom_of_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def _scroll_to_element(self, locator=None, element=None):
        if element:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        else:
            self.driver.execute_script("arguments[0].scrollIntoView();", self._find(locator))

    def _scroll_to_top_of_page(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def _type(self, locator, input_text, clear_input=False, terminate_with_return_key=False):
        input_element = self._find_clickable_element(locator)

        if clear_input:
            input_element.clear()

        input_element.send_keys(input_text)

        if terminate_with_return_key:
            input_element.send_keys(Keys.RETURN)

    def _visit(self, url):
        self.driver.get(url)

    def _wait_for_element_to_appear(self, locator=None, element=None, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        if element:
            wait.until(expected_conditions.visibility_of(element))
        elif locator:
            wait.until(expected_conditions.visibility_of_element_located((locator['by'], locator['value'])))

    def _wait_for_elements_to_appear(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(lambda dr: dr.find_elements(locator['by'], locator['value']))

    def _wait_for_element_to_disappear(self, locator=None, element=None, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        if element:
            wait.until(expected_conditions.invisibility_of_element(element))
        elif locator:
            wait.until(expected_conditions.invisibility_of_element_located((locator['by'], locator['value'])))

    def _wait_for_element_to_disappear_from_dom(self, element, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.staleness_of(element))

    def _wait_for_element_to_be_selected(self, locator=None, element=None, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        if element:
            wait.until(expected_conditions.element_to_be_selected(element))
        elif locator:
            wait.until(expected_conditions.element_located_to_be_selected((locator['by'], locator['value'])))

    def _wait_for_element_attribute_to_contain_value(
        self,
        attribute_name,
        expected_value,
        locator=None,
        element=None,
        timeout=10
    ):
        seconds_waited = 0

        if locator:
            element = self._find(locator)

        while expected_value not in element.get_attribute(attribute_name) and seconds_waited < timeout:
            sleep(1)
            seconds_waited += 1

    def _wait_for_expected_text_to_appear(self, locator, expected_text, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.text_to_be_present_in_element((locator['by'], locator['value']), expected_text))
