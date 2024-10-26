from sqlalchemy.orm import Session
from Bot.database.models import MediaFile


def upload_media_file(db: Session, file_path: str, description: str, user_id: int):
    """Upload a new media file."""
    new_media_file = MediaFile(file_path=file_path, description=description, user_id=user_id)
    db.add(new_media_file)
    db.commit()
    db.refresh(new_media_file)
    return new_media_file


def delete_media_file(db: Session, media_id: int) -> bool:
    """Delete a media file by ID."""
    media_file = db.query(MediaFile).filter(MediaFile.id == media_id).one_or_none()
    if media_file:
        db.delete(media_file)
        db.commit()
        return True
    return False


def list_media_files(db: Session):
    """List all media files."""
    return db.query(MediaFile).all()
