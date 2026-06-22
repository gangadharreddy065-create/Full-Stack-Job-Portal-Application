from app.db.session import engine
from app.db.models import Base


def init_db() -> None:
    Base.metadata.create_all(bind=engine)

