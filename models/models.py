from sqlalchemy import Column, Integer, Float, Boolean, Text, JSON, ForeignKey
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import relationship, DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Role(Base):
    __tablename__: str = 'roles'
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    name: Column = Column(Text(20), unique=True, nullable=False)
    description: Column = Column(Text(100))
    users = relationship('User', back_populates='role')


class User(Base):
    __tablename__: str = 'users'
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    tg_id: Column = Column(Integer, unique=True, nullable=False)
    role_id: Column = Column(Integer, ForeignKey('roles.id'), nullable=False)
    role = relationship('Role', back_populates='users')
    contexts = relationship('Context', back_populates='user')


class Context(Base):
    __tablename__: str = 'contexts'
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    user_id: Column = Column(Integer, ForeignKey('users.id'), nullable=False)
    temperature: Column = Column(Float, nullable=False)
    messages: Column = Column(JSON)
    user = relationship('User', back_populates='contexts')
