from pytest_bdd import given, scenario, then, when
from pytest_bdd.parsers import parse

from europython.factories import ArticleFactory


# Scenarios

@scenario('blog.feature', "Reading an article")
def test_read_article():
    pass


# Requirements

@given(parse("I wrote {count:d} articles"))
def articles(count, db):
    return ArticleFactory.create_batch(count)


# Actions

@when("I access to my blog")
def go_to_homepage(browser, server):
    browser.visit(server.url)


@when("I click on the first article's title")
def go_to_first_article(browser):
    article = browser.find_by_css('.article-list__title').first
    article.click()


# Assertions

@then("I should be redirected to the article's page")
def should_be_redirected(articles, browser):
    article = articles[0]  # We are reading the first article
    assert article.title in browser.title


@then("I should see the article's content")
def should_see_content(articles, browser):
    article = articles[0]  # We are reading the first article
    assert browser.is_text_present(article.content)
