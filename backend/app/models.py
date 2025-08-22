from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship, DeclarativeBase
from datetime import datetime
import enum

class Base(DeclarativeBase):
    pass

class ScanStatus(enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

class Scan(Base):
    __tablename__ = 'scans'

    id = Column(String, primary_key=True)
    target_url = Column(String, nullable=False)
    status = Column(Enum(ScanStatus), default=ScanStatus.PENDING)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime)

    logs = relationship("Log", back_populates="scan", cascade="all, delete-orphan")
    report = relationship("Report", uselist=False, back_populates="scan", cascade="all, delete-orphan")

class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    scan_id = Column(String, ForeignKey('scans.id'), nullable=False)
    agent_name = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    scan = relationship("Scan", back_populates="logs")

class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    scan_id = Column(String, ForeignKey('scans.id'), unique=True, nullable=False)
    data = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    scan = relationship("Scan", back_populates="report")