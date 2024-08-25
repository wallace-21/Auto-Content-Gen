from sqlalchemy import create_engine                                                                                                                from sqlalchemy.ext.declarative import declarative_base                                                                                             from sqlalchemy.orm import sessionmaker, scoped_session                                                                                             import os                                                                                                                                           from dotenv import load_dotenv

"""
Database configuration and session management.

This module handles the creation of the database engine, session management,
and provides utility functions for database operations.

Modules:
    sqlalchemy: SQLAlchemy library used for ORM and session management.
    os: Used to retrieve environment variables.
    dotenv: Used to load environment variables from the .env file.

Classes:
    DBSession: Context manager for handling database sessions.

Functions:
    get_db: Provides a new instance of DBSession for database operations.
"""

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

# Create an engine that connects to the specified database URL
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Create a base class for our class definitions
Base = declarative_base()

# Add query property to the base class
Base.query = SessionLocal.query_property()

class DBSession:
    """
    Handles the opening and closing of database sessions.
    
    Methods:
        __enter__: Opens a new session.
        __exit__: Closes the session.
    """
    def __enter__(self):
        self.db = SessionLocal()
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()

def get_db():
    """
    Provides a new instance of DBSession for database operations.

    Returns:
        DBSession: An instance of DBSession for use in database operations.
    """
    return DBSession()
