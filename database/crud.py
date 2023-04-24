from sqlalchemy.orm import Session

from database.session import SessionLocal


def get_db() -> Session:
    """
        Get session.
    :return: object Session
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
