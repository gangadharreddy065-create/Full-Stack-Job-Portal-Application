from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.init_db import init_db
from app.db.session import SessionLocal
from app.db.models import Application
from app.routers.dependencies import get_current_user

router = APIRouter()


class ApplyPayload(BaseModel):
    job_id: int
    cover_letter: str


@router.post("", status_code=status.HTTP_201_CREATED)
def apply(payload: ApplyPayload, db: Session = Depends(lambda: SessionLocal()), user=Depends(get_current_user)) -> dict:
    init_db()

    # prevent duplicate application
    existing = (
        db.query(Application)
        .filter(Application.user_id == user.id, Application.job_id == payload.job_id)
        .first()
    )
    if existing:
        raise HTTPException(status_code=400, detail="Already applied")

    app_obj = Application(user_id=user.id, job_id=payload.job_id, cover_letter=payload.cover_letter)
    db.add(app_obj)
    db.commit()
    db.refresh(app_obj)
    return {"id": app_obj.id}


@router.get("/mine")
def my_applications(db: Session = Depends(lambda: SessionLocal()), user=Depends(get_current_user)) -> list[dict]:
    init_db()
    apps = db.query(Application).filter(Application.user_id == user.id).order_by(Application.created_at.desc()).all()
    return [
        {"id": a.id, "job_id": a.job_id, "cover_letter": a.cover_letter, "created_at": a.created_at}
        for a in apps
    ]

