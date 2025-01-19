from app.models.database import db
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

def check_health():
    try:
        with db.engine.connect() as conn:
            conn.execute(text('SELECT 1'))
        return True, "Database connection successful"
    except SQLAlchemyError as e:
        return False, f"Database connection failed"