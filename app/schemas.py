from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    doctor_id: int
    patient_name: str
    start_time: datetime
    end_time: datetime

class AppointmentOut(AppointmentCreate):
    id: int

    class Config:
        orm_mode = True
