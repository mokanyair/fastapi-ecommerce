from fastapi import Depends, HTTPException, status
from app.db.session import SessionLocal


def get_current_user():
    # fake user for now
    user = {"id": 1, "is_active": True}

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )
    return user

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()