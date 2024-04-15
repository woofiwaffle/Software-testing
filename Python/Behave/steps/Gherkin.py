from behave import *

use_step_matcher("re")


@given("I am on the login page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: Given I am on the login page')


@when("I enter my username and password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: When I enter my username and password')


@step("click the login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: And click the login button')


@then("I should be redirected to the homepage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(u'STEP: Then I should be redirected to the homepage')