import pytest
from pytest_bdd import given, when, then

import page_factory as pf


@pytest.fixture(scope='function')
def context():
    return {}


def test_edit_my_profile(context):
    pass


@given('The profile has: name "Anna Smith" ,email "anna.smith@example.com", interests "coding"')
def activate_page_factory():
    context['page_factory'] = pf.PageFactory()


@when("To edit to: 'name': 'Gabi','email': 'GabiDaCoder@gmail.com','interests': 'Coding / Debugging'")
def edit_profile():
    context['page_home'].edit_profile_button()
    context['page_home'].name_editor()
    context['page_home'].email_editor()
    context['page_home'].interest_editor()
    context['page_home'].update_profile_button()


@then("DB will hold new info")
def compare_data():
    context['page_home'].get_data_from_mongo_express()
    assert context['page_home'].mongo_name() == pf.DATA_FOR_EDIT['name']
    assert context['page_home'].mongo_email() == pf.DATA_FOR_EDIT['email']
    assert context['page_home'].mongo_interest() == pf.DATA_FOR_EDIT['interests']
