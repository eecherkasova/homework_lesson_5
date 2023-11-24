import pytest
import selene
import os.path
from selene import be, have
from selene import browser


def test_demoqa():
    browser.open('/')
    browser.element('[id="firstName"]').should(be.blank).type('Liza')
    browser.element('[id="lastName"]').should(be.blank).type('Cherkasova')
    browser.element('[id="userEmail"]').should(be.blank).type('cherkasova@mail.ru')
    browser.element('[id="gender-radio-2"]').double_click()
    browser.element('[id="userNumber"]').should(be.blank).type('9046379219')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__month-select"]').click().type('September').press_enter()
    browser.element('[class="react-datepicker__year-select"]').click().type('1990').press_enter()
    browser.element('[class="react-datepicker__day react-datepicker__day--025"]').click()
    browser.element('[id="subjectsInput"]').should(be.blank).type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('photo/picture.jpg'))
    browser.element('[id="currentAddress"]').should(be.blank).type('Nevskiy avenue, 75')
    browser.element('[id="react-select-3-input"]').should(be.blank).type('NCR').press_enter()
    browser.element('[id="react-select-4-input"]').should(be.blank).type('Delhi').press_enter()
    browser.element('[id="submit"]').press_enter()

    browser.element('[id="example-modal-sizes-title-lg"]').should(have.exact_text('Thanks for submitting the form'))
    browser.all('tbody tr td:last-child').should(
        have.exact_texts('Liza Cherkasova', 'cherkasova@mail.ru', 'Female', '9046379219', '25 September,1990', 'Maths',
                         'Sports, Music', 'picture.jpg', 'Nevskiy avenue, 75', 'NCR Delhi'))
