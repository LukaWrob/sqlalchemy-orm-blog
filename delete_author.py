from models import Author, Article
from session import session


def main():
    author = session.query(Author).get(1)
    assert author is not None, "Author with id 1 not found"

    articles_count = len(author.articles)
    assert articles_count != 0, "Author has no articles"

    session.delete(author)
    session.commit()

    assert session.query(Author).get(1) is None, "Author not deleted"

    articles = session.query(Article).filter_by(
        author_id=author.id
    )
    assert len(articles.all()) == 0, "Author's articles not deleted"


if __name__ == "__main__":
    main()
