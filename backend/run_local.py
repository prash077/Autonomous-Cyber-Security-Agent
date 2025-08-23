import os
from flask import Flask
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Enum, create_engine
from sqlalchemy.orm import relationship, DeclarativeBase, sessionmaker
from datetime import datetime
import enum
from agents.crew import SecurityCrew

load_dotenv()

class Base(DeclarativeBase):
    pass

engine = create_engine(os.environ.get("DATABASE_URL"))
Session = sessionmaker(bind=engine)

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

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    @app.route("/run-crew")
    def run_crew():
        target_url = "http://example.com"
        crew_runner = SecurityCrew(target_url)
        result = crew_runner.run()
        return {"result": str(result)}
    return app

app = create_app()

if __name__ == "__main__":
    print("Creating database tables...")
    with app.app_context():
        Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")
    
    app.run(debug=True)