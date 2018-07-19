from pytest_bdd import given, scenario, then, when
from pytest_bdd.parsers import parse


# Scenarios

@scenario('blog.feature', "Reading an article")
def test_read_article():
    pass


# Requirements

# FIXME: Use Pytest-BDD parser, again.
# For an unknown reason, parsers stopped to work properly (as of 06/08/2018),
# leading to a "Step definition not found" error. See:
# https://travis-ci.org/arugifa/ep2018-workshop/builds/411806000
#
# from pytest_bdd.parsers import parse
# @given(parse("I wrote {count:d} articles"))

@given("I wrote 3 articles")
def articles(db):
    raise NotImplementedError


# Actions

@when("I access to my blog")
def go_to_homepage(browser, server):
    raise NotImplementedError


@when("I click on the first article's title")
def go_to_first_article(browser):
    raise NotImplementedError


# Assertions

@then("I should be redirected to the article's page")
def should_be_redirected(articles, browser):
    raise NotImplementedError


@then("I should see the article's content")
def should_see_content(articles, browser):
    raise NotImplementedError
