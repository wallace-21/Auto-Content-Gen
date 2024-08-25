from sqlalchemy import Column, Integer, String, Text
from database import Base  


"""
Database model for the 'articles' table.

This module defines the structure of the 'articles' table in the database,
which includes fields for storing article links and their summaries.

Modules:
    sqlalchemy: SQLAlchemy library used for ORM and table definitions.

Classes:
    Article: Represents the structure of the 'articles' table in the database.
"""


class Article(Base):
    """
    Represents an article in the database.

    Attributes:
        id (int): The primary key for the article.
        link (str): The URL of the article.
        summary (str): A summary of the article.
    """
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    link = Column(String, nullable=False)
    summary = Column(Text)

    def __repr__(self):
        """
        Provides a string representation of the Article instance.
        
        Returns:
            str: A string representation of the article.
        """
        return f"<Article(id={self.id}, link='{self.link}', summary='{self.summary[:30]}...')>"
