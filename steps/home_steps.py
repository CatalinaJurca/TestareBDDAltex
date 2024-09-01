from behave import *

@given ('I am on the Altex homepage')
def step_impl(context):
    context.home_page.navigate_to_homepage()
    context.home_page.accept_cookies()