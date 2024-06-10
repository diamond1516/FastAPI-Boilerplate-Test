from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)