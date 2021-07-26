import time
from random import randint
from registration_page import Registration


# A005, CON_TC02_Sikeres regisztráció, még nem létező felhasználói adatokkal.
def test_registration():
    registration = Registration()
    time.sleep(3)

    # sign up
    random_user = f"Micky{randint(1, 200)}"
    reg_input_data = [random_user, f"{random_user}@gmail.com", "12ABab@&"]
    expected_login_nav_bar_elements = ['Home', ' New Article', ' Settings', reg_input_data[0], ' Log out']
    expected_msg_title_ok = 'Welcome!'
    expected_registration_successful = 'Your registration was successful!'

    registration.locator(registration.reg_xp).click()
    time.sleep(3)
    registration.locators(registration.nav_bar_links_xp)

    input_fields = registration.locators_tag_name(registration.input_fields_tag_name)
    time.sleep(5)
    registration.fill_input_fields(reg_input_data, input_fields)

    registration.swal_handling(expected_msg_title_ok, expected_registration_successful)
    time.sleep(3)
    registration.compare_the_text_of_two_lists(
        registration.locators(registration.nav_bar_links_xp), expected_login_nav_bar_elements)  # check login

    time.sleep(3)
    registration.locator(registration.logout_xp).click()  # logout
    time.sleep(3)


# A002, CON_TC24_Regisztráció validátorok ellenőrzése (üres form, helytelen formátumú password)
def test_reg_validators1():
    registration = Registration()
    time.sleep(3)
    registration.locator(registration.reg_xp).click()  # sign up

    # check that the 3 input fields are displayed
    input_fields = registration.locators_tag_name(registration.input_fields_tag_name)
    expected_input_fields = ["Username", "Email", "Password"]
    assert len(input_fields) == 3
    registration.compare_two_lists_items(input_fields, "placeholder", expected_input_fields)

    # check have_an_account_link, sign_up_btn
    registration.displayed_and_enabled(registration.have_an_account_link_xp)
    registration.displayed_and_enabled(registration.sign_up_btn_xp)

    # check password format validation message
    random_user = f"tester{randint(1, 200)}"
    reg_input_data = [random_user, f"{random_user}@gmail.com", "ABCabc1"]
    expected_msg_title = 'Registration failed!'
    expected_msg_pwd_text = 'Password must be 8 characters long and include 1 number, 1 uppercase letter, and 1 ' \
                            'lowercase letter.'

    registration.fill_input_fields(reg_input_data, input_fields)
    registration.swal_handling(expected_msg_title, expected_msg_pwd_text)
    time.sleep(3)
    registration.check_input_fields_fill_in(input_fields)

    # EMPTY FORM : check empty validation message
    expected_empty_form_msg_text = 'Username field required.'

    registration.locator(registration.sign_up_btn_xp).click()  # sign_up_btn.click
    registration.swal_handling(expected_msg_title, expected_empty_form_msg_text)
    time.sleep(3)
    registration.check_input_fields_fill_in(input_fields)


# A003, CON_TC03_Regisztráció validátorok ellenőrzése (regisztráció helytelen email formátummal)
def test_reg_validators2():
    registration = Registration()
    time.sleep(3)
    random_user = f"Sancho{randint(4, 100)}"
    reg_input_data = [random_user, f"{random_user}@gmailcom", "12ABab@&"]
    expected_msg_title = 'Registration failed!'
    expected_email_format_msg_text = 'Email must be a valid email.'

    registration.locator(registration.reg_xp).click()  # sign up
    input_fields = registration.locators_tag_name(registration.input_fields_tag_name)
    time.sleep(3)
    registration.fill_input_fields(reg_input_data, input_fields)
    registration.swal_handling(expected_msg_title, expected_email_format_msg_text)  # check validator
    time.sleep(3)
    registration.check_input_fields_fill_in(input_fields)


# A004, CON_TC23_Sikertelen regisztráció, már regisztrált email fiókkal
def test_reg_validators3():
    registration = Registration()
    time.sleep(3)
    # successful registration
    random_user = f"Fletch{randint(100, 200)}"
    reg_input_data = [random_user, f"{random_user}@gmail.com", "12ABab@&"]

    registration.locator(registration.reg_xp).click()  # sign up
    time.sleep(3)
    input_fields = registration.locators_tag_name(registration.input_fields_tag_name)
    registration.fill_input_fields(reg_input_data, input_fields)
    registration.locator(registration.swal_btn_xp).click()
    time.sleep(3)
    registration.locator(registration.logout_xp).click()  # logout
    time.sleep(3)

    # repeated registration
    expected_msg_title = 'Registration failed!'
    expected_email_msg_text = 'Email already taken.'

    registration.locator(registration.reg_xp).click()  # sign_up link
    time.sleep(3)
    registration.fill_input_fields(reg_input_data, input_fields)
    time.sleep(5)
    registration.swal_handling(expected_msg_title, expected_email_msg_text)  # check validator
    time.sleep(3)
    registration.check_input_fields_fill_in(input_fields)

    registration.teardown()