from sqlalchemy import Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from database import Base

# user-group class
class UserGroup(Base):
    __tablename__ = "user_groups"
    user_id = Column(Integer, primary_key=True)
    group_id = Column(Integer, primary_key=True)
    group_name=Column(String)

    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'group_id'),
    )

#user-activity class
class UserActivity(Base):
    __tablename__ = "user_activity"
    report_date_yyyymmdd = Column(String)
    user_id = Column(Integer, ForeignKey("user_groups.user_id"), primary_key=True)
    lecture_id = Column(Integer, primary_key=True)
    watched_seconds = Column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'lecture_id'),
    )