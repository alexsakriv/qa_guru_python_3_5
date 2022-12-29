import pytest
from selene.support.shared import browser
from selene import command, have


def test_submit():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Aleksandra')
    browser.element('#lastName').type('Krivoruchenko')
    browser.element('#userEmail').type('test@test.com')
    browser.element('#gender-radio-2').with_(click_by_js=True).click()
    browser.element('#userNumber').type('892212124534')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="10"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1997"]').click()
    browser.element('.react-datepicker__day react-datepicker__day--011').with_(click_by_js=True).click()
    browser.element('#lastName').type('Krivoruchenko')