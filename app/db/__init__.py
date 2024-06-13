from app.db.base import Base
from app.db.session import engine


MetaData = Base.metadata
Base.metadata.create_all(bind=engine)
