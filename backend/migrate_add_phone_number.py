from sqlalchemy import inspect, text

from app.db.init_db import init_db
from app.db.session import engine


def migrate() -> None:
    init_db()

    inspector = inspect(engine)
    columns = {column["name"] for column in inspector.get_columns("users")}

    if "phone_number" in columns:
        print("phone_number column already exists.")
        return

    with engine.begin() as connection:
        connection.execute(
            text("ALTER TABLE users ADD COLUMN phone_number VARCHAR(20) NOT NULL DEFAULT ''")
        )

    print("Added phone_number column to users table.")


if __name__ == "__main__":
    migrate()
