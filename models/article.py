from sqlalchemy import Column, Integer, String, Text
from database import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    link = Column(String, nullable=False)
    summary = Column(Text)

    def __repr__(self):
        return f"<Article(id={self.id}, link='{self.link}', summary='{self.summary[:30]}...')>"

