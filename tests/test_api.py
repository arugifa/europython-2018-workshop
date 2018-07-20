from europython.factories import ArticleFactory


def test_get_articles(client, db):
    articles = ArticleFactory.create_batch(2)
    response = client.get('/api/articles/').json

    for actual, expected in zip(response, articles):
        assert actual['id'] == expected.id
        assert actual['title'] == expected.title
