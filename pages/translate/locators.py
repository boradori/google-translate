from selenium.webdriver.common.by import By

CLEAR_SOURCE_TEXT_BUTTON = {
    'by': By.XPATH,
    'value': '//button[@aria-label="Clear source text"]'
}

MORE_SOURCE_LANGUAGES = {
    'by': By.XPATH,
    'value': '//h1[@id="ucj-2"]/following-sibling::div[1]//button[@aria-label="More source languages"]'
}

MORE_SOURCE_LANGUAGES_DROPDOWN = {
    'by': By.XPATH,
    'value':
        (
            '//c-wiz[@class="bvzp8c Tht3fc"]//div[@class="pEyuac X4hZJc"]//div[@class="F29iQc F5Ibjf"]'
            '/following-sibling::div'
        )
}

MORE_TARGET_LANGUAGES = {
    'by': By.XPATH,
    'value': '//h1[@id="ucj-2"]/following-sibling::div[1]//button[@aria-label="More target languages"]'
}

MORE_TARGET_LANGUAGES_DROPDOWN = {
    'by': By.XPATH,
    'value':
        (
            '//c-wiz[@class="bvzp8c DlHcnf"]//div[@class="pEyuac X4hZJc"]//div[@class="F29iQc F5Ibjf"]'
            '/following-sibling::div'
        )
}

SCREEN_KEYBOARD = {
    'by': By.XPATH,
    'value': '//div[@dir="ltr"][2]'
}

SCREEN_KEYBOARD_CLOSE = {
    'by': By.XPATH,
    'value': '//div[@dir="ltr"][1]/div[2]'
}

SCREEN_KEYBOARD_LEFT_SHIFT_KEY = {
    'by': By.XPATH,
    'value': '//div[@dir="ltr"][2]//button[@id="K16"][1]'
}

SELECT_INPUT_TOOL = {
    'by': By.XPATH,
    'value': '//a[@aria-label="Show the Input Tools menu"]'
}

SELECTED_SOURCE_LANGUAGE = {
    'by': By.XPATH,
    'value': '//div[@class="ccvoYb EjH7wc"]/div[1]//div[@class="akczyd"][1]//button[@aria-selected="true"]'
}

SELECTED_TARGET_LANGUAGE = {
    'by': By.XPATH,
    'value': '//div[@class="ccvoYb EjH7wc"]/div[1]//div[@class="akczyd"][2]//button[@aria-selected="true"]'
}

SOURCE_FIELD = {
    'by': By.XPATH,
    'value': '//textarea[@aria-label="Source text"]'
}

SWAP_LANGUAGES = {
    'by': By.XPATH,
    'value': '//button[contains(@aria-label, "Swap languages")]'
}

TARGET_FIELD = {
    'by': By.XPATH,
    'value': '//div[@aria-live="polite"]//span[@class="Q4iAWc"]'
}

TRANSLATING = {
    'by': By.XPATH,
    'value': '//div[contains(text(), "Translating...")]'
}

US_INTERNATIONAL = {
    'by': By.XPATH,
    'value': '//span[contains(text(), "US International")]'
}


def select_input_tool_by_input_tool_name(input_tool_name):
    return {
        'by': By.XPATH,
        'value': f'//li[@class="ita-kd-menuitem"]/span[text()="{input_tool_name}"]'
    }


def select_screen_keyboard_key_by_key_name(key_name):
    return {
        'by': By.XPATH,
        'value': f'//div[@dir="ltr"][2]//button/span[text()="{key_name}"]'
    }


def select_source_language_by_language_name(language_name):
    return {
        'by': By.XPATH,
        'value':
            (
                '//c-wiz[@class="bvzp8c Tht3fc"]//div[@class="pEyuac X4hZJc"]//div[@class="F29iQc F5Ibjf"]'
                f'/following-sibling::div//div[text()="{language_name}"]'
            )
    }


def select_target_language_by_language_name(language_name):
    return {
        'by': By.XPATH,
        'value':
            (
                '//c-wiz[@class="bvzp8c DlHcnf"]//div[@class="pEyuac X4hZJc"]//div[@class="F29iQc F5Ibjf"]'
                f'/following-sibling::div//div[text()="{language_name}"]'
            )
    }


def select_target_text_by_target_text_and_source_text(target_text, source_text):
    return {
        'by': By.XPATH,
        'value':
            (
                '//div[@aria-live="polite"]//span[@class="Q4iAWc"]/following-sibling::div'
                f'//div[text()="{target_text}"]/following-sibling::div[text()="{source_text}"]'
            )
    }
