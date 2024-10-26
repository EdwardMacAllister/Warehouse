from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MediaFile(Base):
    __tablename__ = 'media_files'

    id = Column(Integer, primary_key=True, index=True)
    file_path = Column(String, index=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))  # Assuming there's a User model

    def __repr__(self):
        return f"<MediaFile(file_path={self.file_path}, description={self.description})>"
