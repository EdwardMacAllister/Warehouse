from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Replace it with your actual database URL
DATABASE_URL = "sqlite:///./warehouse.db"  # Example for SQLite

# Create the database engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_db():
    """Dependency that yields a database session."""
    db = SessionLocal()  # Create a new session
    try:
        yield db  # This allows the session to be used in a context manager
    finally:
        db.close()  # Ensure the session is closed after use
