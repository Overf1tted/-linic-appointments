from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/appointments",
    response_model=schemas.AppointmentOut,
    summary="Создать новую запись к врачу"
)
def create_appointment(
    appointment: schemas.AppointmentCreate,
    db: Session = Depends(get_db)
):
    return crud.create_appointment(db, appointment)


@router.get(
    "/appointments/{appointment_id}",
    response_model=schemas.Appointment,
    summary="Получить запись по ID"
)
def read_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):
    db_appointment = crud.get_appointment(db, appointment_id)
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment
