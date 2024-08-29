from behave import *

@given ('I am on the Altex homepage')
def step_impl(context):
    context.home_page.navigate_to_homepage()

@when("I go to the contact form")
def step_impl(context):
    context.home_page.click_contact()

@when('I fill the required fields without one')
def step_impl(context):
    context.contact_page.contact_form()

@then('The page is not changing')
def step_impl(context):
    context.contact_page.check_page()