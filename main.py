from database import engine, Base, get_db
from models.article import Article

# Create the tables if they don't exist
Base.metadata.create_all(engine)

# CRUD Operations
def crud_operations():
    with get_db() as db:
        # Insert a new article
        new_article = Article(link='https://wallacenews.com/article1', summary='Summary of article 1')
        db.add(new_article)
        db.commit()

        # Get all articles
        articles = db.query(Article).all()
        print(articles)
        print(articles)

        # Update an article
        article_to_update = db.query(Article).filter_by(id=1).first()
        article_to_update.summary = 'Updated summary of article 1'
        db.commit()

        # Delete an article
        article_to_delete = db.query(Article).filter_by(id=1).first()
        db.delete(article_to_delete)
        db.commit()

if __name__ == "__main__":
    crud_operations()
