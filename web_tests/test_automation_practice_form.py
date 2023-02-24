import pytest
from selene.support.shared import browser
from selene import command, have, be


def test_submit():
    # GIVEN
    browser.open('https://demoqa.com/automation-practice-form')

    # WHEN
    browser.element('#firstName').type('Aleksandra')
    browser.element('#lastName').type('Krivoruchenko')
    browser.element('#userEmail').type('test@test.com')
    browser.element('[name=gender][value=Female]+label').click()
    browser.element('#userNumber').type('8922121245')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="11"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1997"]').click()
    browser.element('.react-datepicker__week>.react-datepicker__day--011').click()
    # browser.element('#subjectsContainer').click()
    # browser.element('#subjectsInput').type('computer')
    # browser.element('//*[class="subjects-auto-complete__menu"]//div[.//*[.="Computer Science"]]').click()
    browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Sports'))
    browser.all('[id^=hobbies-checkbox]').element_by(have.exact_text('Reading'))
    browser.all('[id^=hobbies-checkbox]').element_by(have.exact_text('Music'))


    # THEN