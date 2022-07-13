import pytest

from pages import (
    TranslatePage
)


@pytest.fixture(scope='session')
def translate_page(session_driver):
    return TranslatePage(session_driver)
