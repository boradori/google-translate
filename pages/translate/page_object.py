import logging
import time

from . import locators
from pages.base_page import BasePage


class TranslatePage(BasePage):
    @property
    def more_source_languages_btn(self):
        return self._find_clickable_element(locators.MORE_SOURCE_LANGUAGES)

    @property
    def more_target_languages_btn(self):
        return self._find_clickable_element(locators.MORE_TARGET_LANGUAGES)

    @property
    def screen_keyboard(self):
        return self._find_visible_element(locators.SCREEN_KEYBOARD)

    @property
    def selected_source_language(self):
        return self._get_inner_text_from_elements(locators.SELECTED_SOURCE_LANGUAGE)[0]

    @property
    def selected_target_language(self):
        return self._get_inner_text_from_elements(locators.SELECTED_TARGET_LANGUAGE)[0]

    @property
    def source_field(self):
        return self._find_visible_element(locators.SOURCE_FIELD)

    @property
    def target_field(self):
        return self._find_visible_element(locators.TARGET_FIELD)

    def clear_source_text(self):
        logging.info('Clearing "Source text" field.')
        self._click(locators.CLEAR_SOURCE_TEXT_BUTTON)

    def click_screen_keyboard_key_by_key_name(self, key_name):
        logging.info(f'Clicking key, "{key_name}".')
        self._click(locators.select_screen_keyboard_key_by_key_name(key_name))

    def click_swap_languages_btn(self):
        logging.info('Clicking "Swap languages" button.')
        self._click(locators.SWAP_LANGUAGES)
        self._pause_for_animation()

    def close_screen_keyboard(self):
        logging.info('Closing "Screen keyboard".')
        self._click(locators.SCREEN_KEYBOARD_CLOSE)

    def enter_source_text(self, source_text):
        logging.info(f'Entering source text: "{source_text}".')
        self._type(locators.SOURCE_FIELD, source_text)
        self.wait_for_translation_to_finish()

    def navigate(self):
        logging.info('Navigating to "Google Translate" page.')
        self._visit('https://translate.google.com')

    def select_source_language_by_language_name(self, language_name):
        logging.info(f'Selecting source language, "{language_name}".')
        self._move_to_element(locator=locators.select_source_language_by_language_name(language_name))
        self._click(locators.select_source_language_by_language_name(language_name))

    def select_target_language_by_language_name(self, language_name):
        logging.info(f'Selecting target language, "{language_name}".')
        self._click(locators.select_target_language_by_language_name(language_name))

    def select_target_text_by_target_text_and_source_text(self, target_text, source_text):
        logging.info(f'Selecting target text of "{target_text}" and source text of "{source_text}".')
        self._click(locators.select_target_text_by_target_text_and_source_text(target_text, source_text))

    def select_us_international_screen_keyboard(self):
        logging.info('Selecting "US International" screen keyboard.')
        self._click(locators.US_INTERNATIONAL)

    def toggle_more_languages(self, source_or_target):
        logging.info(f'Toggling "More {source_or_target} languages".')
        if source_or_target == 'source':
            self._move_to_element(element=self.more_source_languages_btn)
            self.more_source_languages_btn.click()
        elif source_or_target == 'target':
            self._move_to_element(element=self.more_target_languages_btn)
            self.more_target_languages_btn.click()
            self._pause_for_animation()

    def toggle_screen_keyboard_left_shift_key(self):
        logging.info('Toggling the left "Shift" key on the screen keyboard.')
        self._click(locators.SCREEN_KEYBOARD_LEFT_SHIFT_KEY)

    def toggle_select_input_tool_dropdown(self):
        logging.info('Toggling "Select input tool" dropdown.')
        self._click(locators.SELECT_INPUT_TOOL)

    def toggle_target_text_dropdown(self):
        logging.info('Toggling "Target text" dropdown.')
        self.target_field.click()

    def wait_for_more_languages_dropdown_to_appear(self, source_or_target):
        logging.info(f'Waiting for "More {source_or_target} languages" dropdown to appear.')
        if source_or_target == 'source':
            self._wait_for_element_to_appear(locators.MORE_SOURCE_LANGUAGES_DROPDOWN)
        elif source_or_target == 'target':
            self._wait_for_element_to_appear(locators.MORE_TARGET_LANGUAGES_DROPDOWN)

    def wait_for_more_languages_dropdown_to_disappear(self, source_or_target):
        logging.info(f'Waiting for "More {source_or_target} languages" dropdown to disappear.')
        if source_or_target == 'source':
            self._wait_for_element_to_disappear(locators.MORE_SOURCE_LANGUAGES_DROPDOWN)
        elif source_or_target == 'target':
            self._wait_for_element_to_disappear(locators.MORE_TARGET_LANGUAGES_DROPDOWN)

    def wait_for_translation_to_finish(self):
        logging.info('Translating...')
        self._wait_for_element_to_disappear(locators.TRANSLATING)