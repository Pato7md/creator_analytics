from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TwitchFollower(Base):
    __tablename__ = "twitch_followers"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    from_id = Column(String)
    to_id = Column(String)
    followed_at = Column(TIMESTAMP)
    fetched_at = Column(TIMESTAMP)