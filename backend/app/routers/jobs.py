from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.init_db import init_db
from app.db.session import SessionLocal
from app.db.models import Job
from app.routers.dependencies import get_current_user

router = APIRouter()


class JobCreate(BaseModel):
    title: str
    company: str
    location: str
    description: str
    job_type: str = "Full-time"


from sqlalchemy import or_

@router.get("")
def list_jobs(q: str | None = None, location: str | None = None, db: Session = Depends(lambda: SessionLocal())) -> list[dict]:
    init_db()
    try:
        query = db.query(Job)
        if q:
            terms = q.split()
            for term in terms:
                query = query.filter(
                    or_(
                        Job.title.ilike(f"%{term}%"),
                        Job.description.ilike(f"%{term}%"),
                        Job.company.ilike(f"%{term}%")
                    )
                )
        if location:
            query = query.filter(Job.location.ilike(f"%{location}%"))

        jobs = query.order_by(Job.created_at.desc()).all()
        return [
            {
                "id": j.id,
                "title": j.title,
                "company": j.company,
                "location": j.location,
                "description": j.description,
                "job_type": j.job_type,
                "created_at": j.created_at,
            }
            for j in jobs
        ]
    finally:
        db.close()


@router.get("/{job_id}")
def job_detail(job_id: int, db: Session = Depends(lambda: SessionLocal())) -> dict:
    init_db()
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return {
        "id": job.id,
        "title": job.title,
        "company": job.company,
        "location": job.location,
        "description": job.description,
        "job_type": job.job_type,
        "created_at": job.created_at,
    }


@router.post("", status_code=status.HTTP_201_CREATED)
def create_job(payload: JobCreate, db: Session = Depends(lambda: SessionLocal()), user=Depends(get_current_user)) -> dict:
    # simple: only admin can create
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin only")

    init_db()
    job = Job(**payload.model_dump())
    db.add(job)
    db.commit()
    db.refresh(job)
    return {"id": job.id}

