import os
from selene.support.shared import browser
from selene import command, have
import web_tests


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
    browser.element('.react-datepicker__month-select').send_keys('December')
    browser.element('.react-datepicker__year-select').send_keys('1997')
    browser.element(f'.react-datepicker__day--0{11}').click()

    browser.element('#subjectsInput').click().type('computer')
    browser.all('.subjects-auto-complete__option').element_by(have.exact_text('Computer Science')).click()

    browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Sports')).click()
    browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Reading')).click()
    browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Music')).click()

    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(web_tests.__file__), 'resources/foto.jpeg')
        )
    )

    browser.element('#currentAddress').type('Tyumen, Moskovskaya Street 42')

    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Noida')).perform(command.js.click)

    browser.element('#submit').press_enter()

    # THEN
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Aleksandra Krivoruchenko',
            'test@test.com',
            'Female',
            '8922121245',
            '11 December,1997',
            'Computer Science',
            'Sports, Reading, Music',
            'foto.jpeg',
            'Tyumen, Moskovskaya Street 42',
            'NCR Noida',
        )
    )
