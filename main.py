from flask import Flask, request, jsonify                                                                                                           from database import engine, Base, get_db                                                                                                           from models.article import Article
from services.article_summary import summarize_article


"""
Main entry point for the Social Media AI System.

This module sets up the Flask application, initializes the database,
and includes routes for various functionalities.

Modules:
    flask: Flask framework used for creating the web application.
    database: Contains database setup and session management.
    models.article: Contains the Article model.

Functions:
    index: Returns a welcome message indicating that the system is running.
    create_article: Creates a new article in the database.
    get_articles: Retrieves all articles from the database.
"""


app = Flask(__name__)

# Create the tables if they don't exist
Base.metadata.create_all(engine)

@app.route("/")
def index():
    """
    Root endpoint that returns a welcome message.
    
    Returns:
        dict: A welcome message.
    """
    return jsonify({"message": "Social Media AI System is running"})

@app.route("/articles/", methods=["POST"])
def create_article():
    """
    Creates a new article with a generated summary in the database.
    
    Returns:
        dict: The newly created article details.
    """
    db = get_db().__enter__()
    link = request.json.get("link")
    summary = summarize_article(link)
    new_article = Article(link=link, summary=summary)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    db.__exit__(None, None, None)
    return jsonify({
        "id": new_article.id,
        "link": new_article.link,
        "summary": new_article.summary
    })

@app.route("/articles/", methods=["GET"])
def get_articles():
    """
    Retrieves all articles stored in the database.
    
    Returns:
        list: A list of all articles in the database.
    """
    db = get_db().__enter__()
    articles = db.query(Article).all()
    db.__exit__(None, None, None)
    return jsonify([{
        "id": article.id,
        "link": article.link,
        "summary": article.summary
    } for article in articles])


@app.route("/articles/", methods=["POST"])
def create_article():
    """
    Creates a new article with a generated summary in the database,
    and posts the summary to social media platforms.
    
    Returns:
        dict: The newly created article details and post statuses.
    """
    db = get_db().__enter__()
    link = request.json.get("link")
    summary = summarize_article(link)
    new_article = Article(link=link, summary=summary)
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    db.__exit__(None, None, None)
    
    # Post the summary to social media
    post_responses = post_to_all_platforms(summary)
    
    return jsonify({
        "id": new_article.id,
        "link": new_article.link,
        "summary": new_article.summary,
        "posts": post_responses
    })


if __name__ == "__main__":
    app.run(debug=True)

