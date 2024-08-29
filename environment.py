from pages.contact_page import Contact_Page
from pages.home_page import Home_Page


def before_all(context):
    context.home_page = Home_Page()
    context.contact_page= Contact_Page()