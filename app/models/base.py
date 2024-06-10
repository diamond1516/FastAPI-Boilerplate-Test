from sqlalchemy import Column, Integer, DateTime, func
from app.db.base import Base


class BaseModel(Base):
    __abstract__ = True
    __tablename__ = "basemodel"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

