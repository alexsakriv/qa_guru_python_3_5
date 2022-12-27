import pytest
from selene.support.shared import browser
from selene import command, have


def test_submit():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Aleksandra')
    browser.element('#lastName').type('Krivoruchenko')
    browser.element('#userEmail').type('test@test.com')
    browser.element('#gender-radio-2').click()
    browser.element('#userNumber').type('892212124534')
    browser.element('#dateOfBirthInput').type('11.12.1997')