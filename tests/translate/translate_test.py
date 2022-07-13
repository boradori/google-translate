import pytest
import logging
import json

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@pytest.mark.all
@pytest.mark.translate
class TestTranslate:
    @pytest.fixture(autouse=True)
    def set_up_and_tear_down(self, translate_page, session_driver):
        if "translate.google.com" not in session_driver.current_url:
            translate_page.navigate()

    @pytest.mark.order(1)
    def test_user_can_translate_german_to_spanish(self, translate_page):
        json_file = open('test_data/translation_data.json', 'r')
        json_data = json_file.read()
        translation_data = json.loads(json_data)

        source_language = translation_data['source_language']
        target_language = translation_data['translation_language']
        source_text = translation_data['initial_text']
        target_text = translation_data['expected_result']

        translate_page.toggle_more_languages(source_or_target='source')
        translate_page.wait_for_more_languages_dropdown_to_appear(source_or_target='source')
        translate_page.select_source_language_by_language_name(source_language)

        logging.info(f'Verifying that the selected source language is "{source_language}".')
        expected_result = source_language.upper()
        actual_result = translate_page.selected_source_language
        logging.info(f'Expected result: {expected_result}')
        logging.info(f'Actual result:   {actual_result}')
        assert expected_result == actual_result

        translate_page.toggle_more_languages(source_or_target='target')
        translate_page.wait_for_more_languages_dropdown_to_appear(source_or_target='target')
        translate_page.select_target_language_by_language_name(target_language)

        logging.info(f'Verifying that the selected target language is "{target_language}".')
        expected_result = target_language.upper()
        actual_result = translate_page.selected_target_language
        logging.info(f'Expected result: {expected_result}')
        logging.info(f'Actual result:   {actual_result}')
        assert expected_result == actual_result

        translate_page.enter_source_text(source_text)

        logging.info(f'Verifying that the source field contains "{source_text}".')
        expected_result = source_text
        actual_result = translate_page.source_field.get_attribute('value')
        logging.info(f'Expected result: {expected_result}')
        logging.info(f'Actual result:   {actual_result}')
        assert expected_result == actual_result

        translate_page.toggle_target_text_dropdown()
        translate_page.select_target_text_by_target_text_and_source_text(target_text, source_text)

        logging.info(f'Verifying that translation from "{source_language}" to "{target_language}" is successful.')
        expected_result = target_text
        actual_result = translate_page.target_field.text

        logging.info(f'Expected result: {expected_result}')
        logging.info(f'Actual result:   {actual_result}')
        assert expected_result == actual_result

    @pytest.mark.order(2)
    def test_user_can_swap_languages(self, translate_page):
        translate_page.click_swap_languages_btn()

        json_file = open('test_data/translation_data.json', 'r')
        json_data = json_file.read()
        translation_data = json.loads(json_data)

        source_language = translation_data['translation_language']
        target_language = translation_data['source_language']
        source_text = translation_data['expected_result']
        target_text = translation_data['initial_text']

        logging.info(f'Verifying that the selected source language is "{source_language}".')
        expected_result = source_language.upper()
        actual_result = translate_page.selected_source_language
        logging.info(f'Expected result: {expected_result}')
        logging.info(f'Actual result:   {actual_result}')
        assert expected_result == actual_result

        logging.info(f'Verifying that the selected target language is "{target_language}".')
        expected_result = target_language.upper()
        actual_result = translate_page.selected_target_language
        logging.info(f'Expected result: {expected_result}')
        logging.info(f'Actual result:   {actual_result}')
        assert expected_result == actual_result

        logging.info(f'Verifying that the source field contains "{source_text}".')
        expected_result = source_text
        actual_result = translate_page.source_field.get_attribute('value')
        logging.info(f'Expected result: {expected_result}')
        logging.info(f'Actual result:   {actual_result}')
        assert expected_result == actual_result

        logging.info(f'Verifying that translation from "{source_language}" to "{target_language}" is successful.')
        expected_result = target_text
        actual_result = translate_page.target_field.text

        logging.info(f'Expected result: {expected_result}')
        logging.info(f'Actual result:   {actual_result}')
        assert expected_result == actual_result

    @pytest.mark.order(3)
    def test_user_can_clear_input_and_use_screen_keyboard_to_enter_source_text(self, translate_page):
        translate_page.clear_source_text()
        translate_page.toggle_select_input_tool_dropdown()
        translate_page.select_us_international_screen_keyboard()

        source_text = 'Hi!'

        for char in source_text:
            screen_keyboard = translate_page.screen_keyboard
            try:
                screen_keyboard.find_element(By.XPATH, f'//button/span[text()="{char}"]').click()
            except NoSuchElementException:
                translate_page.toggle_screen_keyboard_left_shift_key()
                screen_keyboard.find_element(By.XPATH, f'//button/span[text()="{char}"]').click()

        translate_page.close_screen_keyboard()

        logging.info(f'Verifying tht "{source_text}" is displayed in both source field and target field.')
        expected_result = source_text
        actual_source_field = translate_page.source_field.get_attribute('value')
        actual_target_field = translate_page.target_field.text

        logging.info(f'Expected result:          {expected_result}')
        logging.info(f'Actual source field text: {actual_source_field}')
        logging.info(f'Actual target field text: {actual_target_field}')
        assert expected_result == actual_source_field == actual_target_field
