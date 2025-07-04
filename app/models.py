from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from .database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(Integer, nullable=False)
    patient_name = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    __table_args__ = (UniqueConstraint('doctor_id', 'start_time'),)
