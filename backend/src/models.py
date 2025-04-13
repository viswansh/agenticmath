from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    oauth_id = Column(String, unique=True)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    grade = Column(String)
    user = relationship("User")

class Plan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    prompt = Column(Text)
    title = Column(String)
    student = relationship("Student")

class Content(Base):
    __tablename__ = "content"
    id = Column(Integer, primary_key=True)
    plan_id = Column(Integer, ForeignKey('plans.id'))
    title = Column(String)
    body = Column(Text)
    progress_status = Column(String, default="not started")
    plan = relationship("Plan")
