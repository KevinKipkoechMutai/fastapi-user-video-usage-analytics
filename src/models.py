from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

# user-group class
class UserGroup(Base):
    __tablename__ = "user_groups"
    user_id = Column(Integer, primary_key=True)
    group_id = Column(Integer)
    group_name=Column(String)

#user-activity class
class UserActivity(Base):
    __tablename__ = "user_activity"
    report_date_yyyymmdd = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_groups.user_id"), primary_key=True)
    lecture_id = Column(Integer)
    watched_seconds = Column(Integer)