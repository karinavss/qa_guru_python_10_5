from selene import browser, be, have
import pytest
import os


def test_demoqa_form():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.open('/')
    browser.element('#firstName').type('Leo')
    browser.element('#lastName').type('Dicaprio')
    browser.element('#userEmail').type('leonardo@gmail.com')
    browser.element("label[for= 'gender-radio-1']").click()
    browser.element('#userNumber').type('89999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__month-select").click().element('option[value="10"]').click()
    browser.element(".react-datepicker__year-select").click().element('option[value="1974"]').click()
    browser.element('.react-datepicker__day--011').click()
    browser.element('#subjectsInput').type("Arts").press_enter()
    browser.element("label[for=hobbies-checkbox-3]").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('picture/Leo.jpeg'))
    browser.element('#currentAddress').type('Wall street 11')
    browser.element('#react-select-3-input').type('Raj').press_enter()
    browser.element('#react-select-4-input').type('Jai').press_enter()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    browser.element('.table').all('td:nth-child(2)').should(have.texts(

        'Leo Dicaprio',
        'leonardo@gmail.com',
        'Male',
        '89999999999',
        '11 November,1974',
        'Arts',
        'Music',
        'Leo.jpeg',
        'Wall street 11',
        'Rajasthan Jaipur'
    ))

