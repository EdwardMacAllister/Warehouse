# utils/db_utils.py
from Bot.database.session import SessionLocal


def get_db_session():
    """
    Creates a new database session.

    :return: SessionLocal instance
    """
    return SessionLocal()


def commit_session(session):
    """
    Commits the current session to the database.

    :param session: Database session
    """
    session.commit()


def close_session(session):
    """
    Closes the database session.

    :param session: Database session
    """
    session.close()
