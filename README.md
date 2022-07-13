# Google Translate Automation
https://translate.google.com

Libraries: selenium, pytest, pytest-order, pytest-html

## Requirements
Install the libraries by running the following command:
```pip install -r requirements.txt```

You will also need `chromedriver` for Google Chrome and `geckodriver` for FireFox.

Recommendation: use virtual environment
```
python -m venv venv
```

```
source venv/bin/activate
```

## Execution:
`pytest -m all` runs all test suites.

`pytest -m translate` should run `translate_test.py`.

Choose the browser of your choice from chrome, firefox, and safari.
Chrome is the default so omitting `--browser` works the same as `--browser chrome`.

```
pytest -m all
```
```
pytest -m all --browser chrome
```
If you want to use firefox, you have to specify `--browser firefox` like below.
```
pytest -m all --browser firefox
```

If you need to generate test report in HTML, add --html FILENAME.html

```
pytest -m all --browser chrome --html htmlreports.html
```

## File Structure
- `pages`: page objects and locators (Page Object Model) are stored.
- `test_data`: translation_data.json is in this folder.
- `tests`: test files are in this folder (each test is in its own folder).

## What does this test suite cover?
The test suite covers some of basic functionalities of Google Translate.

In `test_data` folder, there is a file called, `translation_data.json`,
which contains `source_language`, `translation_language`, `initial_text`, and `expected_result`.

`translate_test.py` uses the JSON file above to translate a German word to Spanish and vice versa.

The last test case is to verify the use of screen keyboard.