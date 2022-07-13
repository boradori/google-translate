from tests import config

pytest_plugins = ['tests.fixtures.driver', 'tests.fixtures.page_objects']


def pytest_addoption(parser):
    # https://docs.python.org/2/library/argparse.html#action
    parser.addoption('--browser', action='store', default='chrome')


def pytest_sessionstart(session):
    config.browser = session.config.getoption('--browser')
    config.base_url = 'https://translate.google.com'
