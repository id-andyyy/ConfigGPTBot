from sqlalchemy import MetaData, Column, Integer, Float, Boolean, JSON, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

metadata = MetaData()

Base = declarative_base(metadata=metadata)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tg_id = Column(Integer, unique=True, nullable=False)
    is_admin = Column(Boolean, default=False)
    contexts = relationship('Context', back_populates='user')


class Context(Base):
    __tablename__ = 'contexts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    temperature = Column(Float, default=0.2, nullable=False)
    messages = Column(JSON)
    user = relationship('User', back_populates='contexts')
