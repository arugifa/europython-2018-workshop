Feature: Blog
    A website where you can read articles.

Scenario: Reading an article
    Given I wrote 3 articles
    When I access to my blog
    And I click on the first article's title
    Then I should be redirected to the article's page
    And I should see the article's content
