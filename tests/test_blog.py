from pytest_bdd import given, scenario, then, when
from pytest_bdd.parsers import parse


# Scenarios

@scenario('blog.feature', "Reading an article")
def test_read_article():
    pass


# Requirements

@given(parse("I wrote {count:d} articles"))
def articles(count, db):
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
