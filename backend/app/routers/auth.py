from fastapi import APIRouter, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.security import create_access_token, hash_password, verify_password
from app.db.init_db import init_db
from app.db.session import SessionLocal
from app.db.models import User

from app.routers.dependencies import get_current_user

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(
    full_name: str = Form(...),
    email: str = Form(...),
    phone_number: str = Form(...),
    password: str = Form(...),
) -> dict:
    # minimal endpoint (for learning). In real apps use Pydantic body models.
    init_db()
    db: Session = SessionLocal()
    try:
        existing = db.query(User).filter(User.email == email).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")

        user = User(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            password_hash=hash_password(password),
            is_admin=False,
        )
        db.add(user)
        db.commit()
        return {"id": user.id, "email": user.email, "phone_number": user.phone_number}
    finally:
        db.close()


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()) -> dict:
    init_db()
    db: Session = SessionLocal()
    try:
        user = db.query(User).filter(User.email == form_data.username).first()
        if not user or not verify_password(form_data.password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = create_access_token(str(user.id), extra_claims={"email": user.email})
        return {"access_token": token, "token_type": "bearer"}
    finally:
        db.close()


@router.get("/me")
def me(user=Depends(get_current_user)) -> dict:
    return {
        "id": user.id,
        "email": user.email,
        "phone_number": user.phone_number,
        "full_name": user.full_name,
        "is_admin": user.is_admin,
    }
