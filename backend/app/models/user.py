from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    streamer_name = Column(String, unique=True, nullable=False)
    twitch_id = Column(String)
    youtube_id = Column(String)
    plan = Column(String)